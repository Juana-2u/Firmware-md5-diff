import os
import sys
import hashlib
import subprocess
from pathlib import Path

def run_binwalk_extract(firmware_path):
    print(f"[*] Extracting {firmware_path} with binwalk...")
    subprocess.run(["binwalk", "-e", firmware_path], check=True)

    filename = os.path.basename(firmware_path)
    extract_dir = f"_{filename}.extracted"
    return extract_dir

def calculate_md5(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def hash_files_in_dir(base_dir):
    file_hashes = {}
    for root, _, files in os.walk(base_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir)
            try:
                file_hashes[rel_path] = calculate_md5(full_path)
            except Exception as e:
                print(f"[-] Failed to hash {rel_path}: {e}")
    return file_hashes

def compare_hashes(hash1, hash2):
    all_keys = set(hash1.keys()).union(hash2.keys())
    differences = []
    for key in sorted(all_keys):
        h1 = hash1.get(key)
        h2 = hash2.get(key)
        if h1 != h2:
            differences.append((key, h1, h2))
    return differences

def main(firmware1, firmware2):
    output_file = "firmware_diff_report.txt"

    # Step 1: 解包
    dir1 = run_binwalk_extract(firmware1)
    dir2 = run_binwalk_extract(firmware2)

    # Step 2: 计算 md5 哈希
    print(f"[*] Calculating MD5 hashes for {dir1}")
    hash1 = hash_files_in_dir(dir1)
    print(f"[*] Calculating MD5 hashes for {dir2}")
    hash2 = hash_files_in_dir(dir2)

    # Step 3: 比较
    print(f"[*] Comparing file hashes and writing to {output_file}...")
    diffs = compare_hashes(hash1, hash2)

    with open(output_file, "w") as f:
        if not diffs:
            f.write("[+] No differences found between the two firmware file systems.\n")
            print("[+] No differences found.")
        else:
            f.write(f"[-] Found {len(diffs)} differing files:\n")
            for path, h1, h2 in diffs:
                f.write(f"\nFile: {path}\n")
                f.write(f"  Firmware 1: {h1 or 'MISSING'}\n")
                f.write(f"  Firmware 2: {h2 or 'MISSING'}\n")
            print(f"[-] Found {len(diffs)} differing files. See '{output_file}' for details.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 compare_firmware_md5.py <firmware1.bin> <firmware2.bin>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])


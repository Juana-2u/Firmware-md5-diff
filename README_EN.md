# Firmware MD5 Diff Tool

Compare two firmware images by unpacking them and generating MD5 hashes of every file in the extracted file systems.

---

## 🚀 Features

- 📦 Automatically unpacks firmware using `binwalk`
- 🔐 Computes `MD5` hashes for every file
- 🧾 Identifies all differing files (new, removed, or modified)
- 📄 Writes a detailed report to `firmware_diff_report.txt`

---

## 🔧 Requirements

- Python 3.6+
- [binwalk](https://github.com/ReFirmLabs/binwalk)

### Optional:
```bash
pip install -r requirements.txt
```

Install binwalk:
```bash
sudo apt install binwalk       # Debian/Ubuntu
brew install binwalk           # macOS
```

---

## 📂 Project Structure

```
firmware-md5-diff/
├── compare_firmware_md5.py       # Main comparison script
├── firmware_diff_report.txt      # Generated output
├── requirements.txt              # Python requirements
├── LICENSE                       # Open-source license
└── README.md                     # Project documentation
```

---

## 🧪 Usage

```bash
python3 compare_firmware_md5.py <firmware_v1.bin> <firmware_v2.bin>
```

### Example Output:
```
[*] Extracting firmware_v1.bin with binwalk...
[*] Extracting firmware_v2.bin with binwalk...
[*] Calculating MD5 hashes...
[*] Comparing file hashes and writing to firmware_diff_report.txt...
[-] Found 4 differing files. See 'firmware_diff_report.txt' for details.
```

---

## 📄 Output: firmware_diff_report.txt

```
[-] Found 4 differing files:

File: etc/passwd
  Firmware 1: 098f6bcd4621d373cade4e832627b4f6
  Firmware 2: 5f4dcc3b5aa765d61d8327deb882cf99

File: bin/busybox
  Firmware 1: a1d0c6e83f027327d8461063f4ac58a6
  Firmware 2: e99a18c428cb38d5f260853678922e03
```

---

## 📜 License

MIT License

You are free to use, modify, and distribute this tool with proper attribution.

---

## 🤝 Contributions

Pull requests welcome! If you find a bug or want to suggest a feature, feel free to open an issue.


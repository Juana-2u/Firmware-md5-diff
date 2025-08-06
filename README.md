# 固件 MD5 差异比较工具

## 项目简介

本项目提供一个 Python 脚本，能够对比两个不同版本的固件镜像中的文件内容差异。脚本使用 binwalk 解包两个固件，并对提取出的文件系统中的所有文件进行 MD5 哈希比对，输出不同文件的哈希信息。

## 功能特点

- 自动使用 `binwalk` 解包固件
- 遍历解包后的文件系统并计算所有文件的 MD5 值
- 对比两个固件中的文件差异
- 将不同的文件及其哈希值输出到 `firmware_diff_report.txt`

## 使用方法

### 环境依赖

确保系统已安装以下工具：

- Python 3
- [binwalk](https://github.com/ReFirmLabs/binwalk)

安装 `binwalk` 示例：
```bash
sudo apt install binwalk
```

### 运行脚本

```bash
python3 compare_firmware_md5.py 固件1.bin 固件2.bin
```

### 输出结果

执行后将在当前目录生成 `firmware_diff_report.txt`，列出所有不同的文件及其在两个固件中的 MD5 值。

示例输出：
```
[-] Found 3 differing files:

File: etc/config/network
  Firmware 1: a1b2c3d4...
  Firmware 2: b2c3d4e5...

File: usr/bin/busybox
  Firmware 1: MISSING
  Firmware 2: a7d8f9e0...
```

## 项目结构

```
.
├── compare_firmware_md5.py     # 主脚本
├── firmware_diff_report.txt    # 差异输出（运行后生成）
```

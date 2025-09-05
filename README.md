# QR Link Generator v1.0
**by frhndevweb.my.id**

Generate QR codes from URLs easily on **Termux** or **Linux**.  
This project is modular, user-friendly, and comes with **two display options**: save QR to your device or show it directly in the terminal.


## 🔹 Features

- ✅ **Download QR directly to device**  
  - QR codes are saved in `/sdcard/Download/` on Termux.
  - Custom file name option available.

- ✅ **Display QR in terminal**  
  - ASCII QR code shown directly in terminal.
  - Works without saving any files.

- ✅ **Smooth UI/UX**
  - Animated loading spinner during generation.
  - Fancy ASCII header with version and author info.

- ✅ **Modular & Expandable**
  - Easy to add features like color QR, batch generation, or other enhancements.

---

## 🔹 Installation (Termux / Linux)

1. **Setup Termux storage** (only first time):
```bash
termux-setup-storage
````

2. **Install Python & pip**
   Termux:

```bash
pkg install python -y
```

Linux (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

3. **Install dependencies**

```bash
pip install "qrcode[pil]"
```

4. **Clone or download the project**

```bash
git clone https://github.com/frhndevweb/link-to-qr.git
cd qr-link-generator
```

5. **Run the program**

```python
python3 main.py
```


## 🔹 How to Use

1. Enter the URL you want to convert to QR code.
2. Choose an option:

   * **1** → Download QR directly to device storage.
   * **2** → Display QR in terminal (ASCII).
3. If downloading, the QR code will be saved in `/sdcard/Download/` (Termux) or the current folder (Linux).



## 🔹 Preview

```
  ____  ____  ____       _      ____                      
 |  _ \|  _ \|  _ \ __ _| | __ |  _ \ ___  ___ ___  _ __  
 | |_) | | | | |_) / _` | |/ / | |_) / _ \/ __/ _ \| '_ \ 
 |  __/| |_| |  __/ (_| |   <  |  _ <  __/ (_| (_) | | | |
 |_|   |____/|_|   \__,_|_|\_\ |_| \_\___|\___\___/|_| |_|

    QR Link Generator v2.1
      by frhndevweb.my.id

Choose option:
1. Download QR to device
2. Display QR in terminal
```



## 🔹 Requirements

* Python 3.x
* `qrcode[pil]` library



## 🔹 License

This project is **free to use**.


## 🔹 Contact

**Author:** frhndevweb.my.id
**GitHub:** [https://github.com/frhndevweb](https://github.com/frhndevweb)

import os
import time
from qr_creator.generator import generate_qr_image, save_qr_to_file
from qr_creator.display import display_qr_terminal

def display_header():
    header = r"""
  ____  ____  ____       _      ____                      
 |  _ \|  _ \|  _ \ __ _| | __ |  _ \ ___  ___ ___  _ __  
 | |_) | | | | |_) / _` | |/ / | |_) / _ \/ __/ _ \| '_ \ 
 |  __/| |_| |  __/ (_| |   <  |  _ <  __/ (_| (_) | | | |
 |_|   |____/|_|   \__,_|_|\_\ |_| \_\___|\___\___/|_| |_|

    QR Link Generator v2.0
      by frhndevweb.my.id
    """
    print(header)

def loading_animation(seconds=1):
    spinner = "|/-\\"
    for i in range(20*seconds):
        print(f"\rGenerating QR... {spinner[i % len(spinner)]}", end="")
        time.sleep(0.05)
    print("\r", end="")

def main():
    display_header()
    
    url = input("Enter URL: ")
    print("\nChoose option:")
    print("1. Download QR to device")
    print("2. Display QR in terminal")
    choice = input("Option (1/2): ").strip()

    img = generate_qr_image(url)
    loading_animation()

    if choice == "1":
        termux_path = "/sdcard/Download"
        if not os.path.exists(termux_path):
            os.makedirs(termux_path)
        filename = os.path.join(termux_path, "link_qr.png")
        save_qr_to_file(img, filename)
        print(f"\nQR Code saved to: {filename}")
    elif choice == "2":
        print("\nQR Code in terminal:\n")
        display_qr_terminal(url)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

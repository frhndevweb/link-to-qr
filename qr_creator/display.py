def display_qr_terminal(url: str):
    """Display QR code directly in terminal using ANSI"""
    try:
        import qrcode
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.make()
        qr.print_ascii(invert=True)
    except ImportError:
        print("qrcode module is required to display QR in terminal")

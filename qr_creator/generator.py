import qrcode
from config.settings import BOX_SIZE, BORDER, FILL_COLOR, BACK_COLOR, DEFAULT_FILENAME

def generate_qr_image(url: str):
    """Generate QR image object (PIL.Image)"""
    qr = qrcode.QRCode(
        version=1,
        box_size=BOX_SIZE,
        border=BORDER
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill=FILL_COLOR, back_color=BACK_COLOR)
    return img

def save_qr_to_file(img, filename=DEFAULT_FILENAME):
    """Save QR to storage"""
    img.save(filename)
    return filename

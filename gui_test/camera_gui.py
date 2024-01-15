import subprocess
from PIL import Image
from pyzbar.pyzbar import decode

def capture_image(image_path='captured_image.jpg'):
    subprocess.run(['libcamera-still', '-n', '-o', image_path])

def read_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    return decoded_objects[0].data.decode() if decoded_objects else ""

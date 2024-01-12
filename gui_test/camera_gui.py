# camera_gui.py
import subprocess
from PIL import Image
from pyzbar.pyzbar import decode
import time
from warehouse import Warehouse


def capture_image(image_path='captured_image.jpg'):
    try:
        subprocess.run(['libcamera-still', '-o', image_path], check=True)
    except subprocess.SubprocessError as e:
        print(f"이미지 캡처 중 오류 발생: {e}")

def read_qr_code(image_path):
    try:
        img = Image.open(image_path)
        decoded_objects = decode(img)
        return decoded_objects[0].data.decode() if decoded_objects else ""
    except IOError as e:
        print(f"이미지 읽기 실패: {e}")
        return ""

def process_data():
    warehouse = Warehouse()
    existing_items = {
        'A12': '차량1',
        'A21': '차량2',
        'A31': '차량3'
    }
    warehouse.load_existing_items(existing_items)

    capture_image('captured_image.jpg')
    qr_data = read_qr_code('captured_image.jpg')

    if qr_data:
        cars = qr_data.split('\n')
        for car in cars:
            if car:
                warehouse.store_item(car)
                print(f"{car}가 {warehouse.store_item(car)}에 저장되었습니다.")
    else:
        print("QR 코드를 읽을 수 없습니다.")

    return warehouse.storage

if __name__ == "__main__":
    main_loop()

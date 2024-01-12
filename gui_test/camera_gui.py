# camera_gui.py
import subprocess
from PIL import Image
from pyzbar.pyzbar import decode
import time

class Warehouse:
    def __init__(self):
        # 창고 구조 초기화
        self.storage = {f'{building}{floor}{room}': None for building in 'ABCD' for floor in range(1, 5) for room in range(1, 3)}

    def load_existing_items(self, existing_items):
        # 미리 저장된 물품 로드
        for location, item in existing_items.items():
            if location in self.storage:
                self.storage[location] = item

    def store_item(self, item):
        # 물품을 저장할 위치 찾기
        for location in self.storage:
            if not self.storage[location]:
                self.storage[location] = item
                return location
        return None

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

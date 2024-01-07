import subprocess
from PIL import Image
from pyzbar.pyzbar import decode
import cv2
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
    # libcamera-still 명령을 사용하여 이미지 캡처
    subprocess.run(['libcamera-still', '-o', image_path])

def read_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    return decoded_objects[0].data.decode() if decoded_objects else ""

# 창고 객체 생성
warehouse = Warehouse()

# 미리 저장된 차량 데이터
existing_items = {
    'A12': '차량1',
    'A21': '차량2',
    'A31': '차량3'
}

def main_loop():
    warehouse = Warehouse()
    existing_items = {
        'A12': '차량1',
        'A21': '차량2',
        'A31': '차량3'
    }
    warehouse.load_existing_items(existing_items)
    qr_code_image_path = 'captured_image.jpg'

    while True:
        capture_image(qr_code_image_path)
        qr_data = read_qr_code(qr_code_image_path)
        # ...(QR 코드 처리 및 출력 코드)
        time.sleep(2)

if __name__ == "__main__":
    main_loop()

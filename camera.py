from PIL import Image
from pyzbar.pyzbar import decode
import cv2

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

# QR 코드 읽기 함수
def read_qr_code(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        decoded_objects = decode(frame)
        if decoded_objects:
            return decoded_objects[0].data.decode()
        cv2.imshow('QR Code Reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC 키를 누르면 종료
            break
    return ""

# 창고 객체 생성
warehouse = Warehouse()

# 미리 저장된 차량 데이터
existing_items = {
    'A12': '차량1',
    'A21': '차량2',
    'A31': '차량3'
}

# 미리 저장된 차량 로드
warehouse.load_existing_items(existing_items)

# 카메라 캡처 객체 생성
cap = cv2.VideoCapture(0)

try:
    # QR 코드 읽기
    print("QR 코드를 카메라 앞에 보여주세요...")
    qr_data = read_qr_code(cap)

    if qr_data:
        # QR 코드 데이터를 개별 차량 데이터로 분리
        cars = qr_data.split('\n')
        
        # 각 차량을 창고에 저장하고 위치 출력
        for car in cars:
            if car:  # 빈 문자열이 아닌 경우에만 처리
                location = warehouse.store_item(car)
                if location:
                    print(f"{car}가 {location}에 저장되었습니다.")
                else:
                    print(f"{car}를 저장할 공간이 없습니다.")
    else:
        print("QR 코드를 읽을 수 없습니다.")

finally:
    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()

# main_test.py
import threading
from warehouse import Warehouse
from gui import create_gui
from qr_processor import process_qr_code

# main
def main():
    print("start")
    # 객체 생성
    warehouse = Warehouse()

    # 미리 저장된 차량 정보
    existing_items = {'A12': '차량1', 'A21': '차량2', 'A31': '차량3'}

    # 미리 저장된 차량 정보 로딩
    warehouse.load_existing_items(existing_items)
    
    # QR 코드 처리 함수 직접 호출
    process_qr_code(warehouse)

    # gui 생성
    create_gui(warehouse)



if __name__ == "__main__":
    main()

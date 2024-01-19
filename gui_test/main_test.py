# main_test.py
import threading
from warehouse import Warehouse
from gui import create_gui
from qr_processor import process_qr_code
from move_position import move_position
from controls.button_clicked import set_warehouse_instance,global_coordinates

# main
def main():
    print("start")
    # 객체 생성
    warehouse = Warehouse()
    
    # 미리 저장된 차량 정보
    existing_items = {'A12': '차량1', 'A21': '차량2', 'A31': '차량3'}
    
    # # 미리 저장된 차량 정보 로딩
    warehouse.load_existing_items(existing_items)

    # 멀티 쓰레딩
    qr_thread = threading.Thread(target=process_qr_code, args=(warehouse,))
    qr_thread.daemon = True
    qr_thread.start()

    set_warehouse_instance(warehouse)

    
    # gui 생성
    create_gui(warehouse)

    x = global_coordinates['x']
    y = global_coordinates['y']
    z = global_coordinates['z']
    move_position(x,y,z)


if __name__ == "__main__":
    main()

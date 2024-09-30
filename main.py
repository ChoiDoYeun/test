# main.py
from gui import create_gui
from warehouse_class import Warehouse
from location_selected_callback import location_selected_callback


def main():
    warehouse = Warehouse()
    # 미리 저장된 차량 정보
    existing_items = {'A21': '중형\n코롤라\nwhite', 'B11': '중형\n라이즈\nblue', 'B21': '중형\n크라운\nwhite', 'C21': '중형\n킥스\norange', 'D32': '대형\n스마일\nsky'}

    # # 미리 저장된 차량 정보 로딩
    warehouse.load_existing_items(existing_items)
    
    create_gui(warehouse, callback=location_selected_callback)
    
if __name__ == "__main__":
    main()

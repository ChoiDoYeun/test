# main.py
from gui import create_gui
from warehouse_class import Warehouse
from location_selected_callback import location_selected_callback


def main():
    warehouse = Warehouse()
    # 미리 저장된 차량 정보
    existing_items = {'A12': 'suv\n산타페\nblue', 'A21': '세단\n아반떼\ngray', 'A31': '세단\n그랜져\nblack'}

    # # 미리 저장된 차량 정보 로딩
    warehouse.load_existing_items(existing_items)
    
    create_gui(warehouse, callback=location_selected_callback)
    
if __name__ == "__main__":
    main()

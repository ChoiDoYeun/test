# location_selected_callback
# 버튼으로 출고기능
from gui import create_gui
from controls.update_labels import update_warehouse_labels
from motor.in_out_mode import output_mode


def location_selected_callback(location, root, warehouse, warehouse_labels):
    print("(main 호출) 저장호수:", location)
    x,y,z = warehouse.calculate_coordinates(location)
    print(" 저장 좌표 {}: x={}, y={}, z={}".format(location, x, y, z))
    output_mode(x,y,z)
    warehouse.remove_item(location)  # 아이템 제거
    #update_warehouse_labels(root, warehouse, warehouse_labels)  # GUI 업데이트
    return location,x,y,z
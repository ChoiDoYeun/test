from move_position import move_position
from motor.calculate_steps_and_direction import calculate_steps_and_direction

# 전역 변수로 Warehouse 인스턴스를 관리하거나, 다른 메커니즘을 사용해야 합니다.
warehouse = None

def set_warehouse_instance(warehouse_instance):
    global warehouse
    warehouse = warehouse_instance

def button_clicked(button_text):
    if warehouse is not None:
        x, y, z = warehouse.calculate_coordinates(button_text)
        move_position(x, y, z)
    else:
        print("Warehouse instance is not set.")

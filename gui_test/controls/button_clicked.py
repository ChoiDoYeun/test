from move_position import move_position
from motor.calculate_steps_and_direction import calculate_steps_and_direction
from warehouse import Warehouse

# 전역 변수로 Warehouse 인스턴스를 관리하거나, 다른 메커니즘을 사용해야 합니다.
warehouse = None
global_coordinates = {'x': 0, 'y': 0, 'z': 0}


def set_warehouse_instance(warehouse_instance):
    global warehouse,global_coordinates
    warehouse = warehouse_instance

def button_clicked(button_text):
    if warehouse is not None:
        x, y, z = warehouse.calculate_coordinates(button_text)
        global_coordinates.update({'x': x, 'y': y, 'z': z})
    else:
        print("Warehouse instance is not set.")

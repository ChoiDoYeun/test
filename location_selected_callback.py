# location_selected_callback
from gui import create_gui
from warehouse_class import Warehouse
from motor.move_position import move_position


def location_selected_callback(location):
    warehouse = Warehouse()
    print("(main 호출) 저장호수:", location)
    x,y,z = warehouse.calculate_coordinates(location)
    print(" 저장 좌표 {}: x={}, y={}, z={}".format(location, x, y, z))
    move_position(x,y,z)
    return location,x,y,z
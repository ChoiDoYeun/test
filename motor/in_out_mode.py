# in_out_mode.py
from warehouse_class import Warehouse
from motor.move_position import move_position_go,move_position_back
from motor.move_item import move_item_high,move_item_low
import time

def input_mode(x,y,z): 
    warehouse = Warehouse()
    move_item_low() # 입차대기장소로 와있는 상태에서 차량을 함으로 이동 # move_item_low 와 move_item_high의 위치는 바뀔수있음
    time.sleep(1)
    print("입차중 : 함에 이동완료")
    move_position_go(x,y,z) # 입차장소로 이동
    time.sleep(1)
    move_item_high() 
    time.sleep(1)
    move_position_back(225,50,350) # 입차대기장소로 이동
    # 차를 함에서 입차장소로 이동
    print("입차 완료")
    time.sleep(1)
    
    
def output_mode(x,y,z):
    warehouse = Warehouse()
    move_position_go(x,y,z) # 저장장소로 이동
    time.sleep(1)
    move_item_high() # 꺼내기
    print("출차중 : 함에 이동완료")
    time.sleep(1)
    move_position_back(225,50,350) # 출차장소로 이동
    time.sleep(1)
    move_item_low()
    print("출차중 : 출차완료")
    time.sleep(1)

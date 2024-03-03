# run.py

from motor.move_position import move_position_back
import time

def run():
    print("Run 시작")
    move_position_back(225,350,50) # 입차대기장소로 이동
    time.sleep(0.5)
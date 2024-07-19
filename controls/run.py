# run.py

from motor.config import initialize, current_x, current_y, current_z,origin_x,origin_y,origin_z
from motor.move_position import move_position_back
from motor.move_origin import move_origin
import time

def run():
    print("Run (원점이동) 시작")
    move_origin(y_step, y_dir, x_step, x_dir, step1_pin, step2_pin, dir1_pin, dir2_pin)
    print("원점이동 완료")
    time.sleep(0.5)

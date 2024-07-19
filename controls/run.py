# run.py

from motor.config import initialize, current_x, current_y, current_z,origin_x,origin_y,origin_z
from motor.move_position import move_position_back
from motor.move_origin import move_origin
import time

def run():
    print("Run (원점이동) 시작")
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2, A_STEP, A_DIR, Con_STEP, Con_DIR, LIMIT_X, LIMIT_Y, LIMIT_Z = initialize()
    move_origin(Y_STEP, Y_DIR, X_STEP, X_DIR, Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2)
    print("원점이동 완료")
    time.sleep(0.5)

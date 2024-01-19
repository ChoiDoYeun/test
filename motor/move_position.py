# move_position.py
import time
from motor.config import initialize, current_x, current_y, current_z
from motor.calculate_steps_and_direction import calculate_steps_and_direction
from motor.move_motor import move_motor

def move_position(target_x, target_y, target_z):
    global current_x, current_y, current_z
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP, Z_DIR = initialize()
    # X축 이동
    steps, direction = calculate_steps_and_direction(current_x, target_x)
    print("x축 이동중")
    move_motor(X_STEP, X_DIR, steps, direction)
    print("x축 이동완료")
    current_x = target_x  # 현재 X 위치 업데이트
    time.sleep(steps * 0.0005)  # 대기 시간
    
    # Y축 이동
    steps, direction = calculate_steps_and_direction(current_y, target_y)
    print("Y축 이동중")
    move_motor(Y_STEP, Y_DIR, steps, direction)
    print("Y축 이동완료")
    current_y = target_y  # 현재 X 위치 업데이트
    time.sleep(steps * 0.0005)  # 대기 시간
    
    # Z축 이동
    steps, direction = calculate_steps_and_direction(current_z, target_z)
    print("Z축 이동중")
    move_motor(Z_STEP, Z_DIR, steps, direction)
    print("Z축 이동완료")
    time.sleep(steps * 0.0005)  # 대기 시간
    
    print("전체 이동완료")
    print("현재위치 :  X = {}, Y = {}, Z = {}".format(current_x, current_y, current_z))
# move_position.py
import time
from motor.config import initialize, current_x, current_y, current_z
from motor.calculate_steps_and_direction import calculate_steps_and_direction
from motor.move_motor import move_motor

def move_position_back(target_x, target_y, target_z):   # x,y->z순으로 동작
    global current_x, current_y, current_z
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP, Z_DIR, A_STEP,A_DIR  = initialize()
    # X축 이동
    steps, direction = calculate_steps_and_direction(current_x, target_x)
    print("x축 이동중")
    move_motor(X_STEP, X_DIR, steps, direction)
    print("x축 이동완료")
    current_x = target_x  # 현재 X 위치 업데이트
    
    # Y축 이동
    steps, direction = calculate_steps_and_direction(current_y, target_y)
    print("Y축 이동중")
    move_motor(Y_STEP, Y_DIR, steps, direction)
    print("Y축 이동완료")
    current_y = target_y  # 현재 Y 위치 업데이트
    time.sleep(0.5)
    
    # Z축 이동
    steps, direction = calculate_steps_and_direction(current_z, target_z)
    print("Z축 이동중")
    move_motor(Z_STEP, Z_DIR, steps, direction)
    print("Z축 이동완료")
    current_z = target_z  # 현재 Z 위치 업데이트
    
    print("전체 이동완료")
    print("현재위치 :  X = {}, Y = {}, Z = {}".format(current_x, current_y, current_z))


def move_position_go(target_x, target_y, target_z):  # z,y->x순으로 동작
    global current_x, current_y, current_z
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP, Z_DIR, A_STEP,A_DIR  = initialize()
    
    # Z축 이동
    steps, direction = calculate_steps_and_direction(current_z, target_z)
    print("Z축 이동중")
    move_motor(Z_STEP, Z_DIR, steps, direction)
    print("Z축 이동완료")
    current_z = target_z  # 현재 Z 위치 업데이트
    
    # Y축 이동
    steps, direction = calculate_steps_and_direction(current_y, target_y)
    print("Y축 이동중")
    move_motor(Y_STEP, Y_DIR, steps, direction)
    print("Y축 이동완료")
    current_y = target_y  # 현재 Y 위치 업데이트
    time.sleep(0.5)
    
    # X축 이동
    steps, direction = calculate_steps_and_direction(current_x, target_x)
    print("x축 이동중")
    move_motor(X_STEP, X_DIR, steps, direction)
    print("x축 이동완료")
    current_x = target_x  # 현재 X 위치 업데이트
    
    print("전체 이동완료")
    print("현재위치 :  X = {}, Y = {}, Z = {}".format(current_x, current_y, current_z))
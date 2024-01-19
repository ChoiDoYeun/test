from motor.init import initialize
from motor.move_motor import move_motor
from motor.calculate_steps_and_direction import calculate_steps_and_direction
from motor.cleanup import cleanup

def move_position(target_x, target_y, target_z):
    initialize()
    # X축 이동
    steps, direction = calculate_steps_and_direction(current_x, target_x) # X축 dir방향, step수 계산
    move_motor(X_STEP, X_DIR, steps, direction) # X축 모터 동작
    time.sleep(steps * 0.002)  # 대기 시간
    current_x = target_x  # 현재 X 위치 업데이트

    # Y축 이동
    steps, direction = calculate_steps_and_direction(current_y, target_y) # Y축 dir방향, step수 계산
    move_motor(Y_STEP, Y_DIR, steps, direction) # Y축 모터 동작
    time.sleep(steps * 0.002)  # 대기 시간
    current_y = target_y  # 현재 Y 위치 업데이트

    # Z축 이동
    steps, direction = calculate_steps_and_direction(current_z, target_z) # Z축 dir방향, step수 계산
    move_motor(Z_STEP, Z_DIR, steps, direction) # Z축 모터 동작
    current_z = target_z  # 현재 Z 위치 업데이트

    # 현재위치 출력
    print("finish move to target position")
    print("current position: X = {}, Y = {}, Z = {}".format(current_x, current_y, current_z))
    
    # 다음 명령을 받기 전에 짧은 시간 대기
    time.sleep(0.5)

    cleanup()

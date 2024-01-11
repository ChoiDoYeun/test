import RPi.GPIO as GPIO
import time

# 모터 드라이버 핀 설정
X_STEP = 17  # X축 STEP 핀 번호
X_DIR = 18   # X축 DIR 핀 번호
Y_STEP = 27  # Y축 STEP 핀 번호
Y_DIR = 22   # Y축 DIR 핀 번호
Z_STEP = 23  # Z축 STEP 핀 번호
Z_DIR = 24   # Z축 DIR 핀 번호

# 스텝 설정
STEPS_PER_MM = 400  # 1mm당 필요한 스텝 수

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup([X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP, Z_DIR], GPIO.OUT)

# 현재위치 초기화
current_x = 0
current_y = 0
current_z = 0

# 모터 동작 함수
def move_motor(step_pin, dir_pin, steps, direction):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.001)  # 1ms 대기
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.001)
      
# dir, step 계산 함수
def calculate_steps_and_direction(current_pos, target_pos):
    if target_pos > current_pos:
        direction = GPIO.HIGH
        steps = (target_pos - current_pos) * STEPS_PER_MM
    else:
        direction = GPIO.LOW
        steps = (current_pos - target_pos) * STEPS_PER_MM
    return steps, direction

try:
    while True:
        # 사용자로부터 X, Y, Z축의 목표 위치 입력 받기
        target_x = float(input("target X : "))
        target_y = float(input("target Y : "))
        target_z = float(input("target Z : "))

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

        # 다음 명령을 받기 전에 짧은 시간 대기
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Before finish, Move to original")
    # 현재 위치에서 (0,0,0)으로 이동
    steps, direction = calculate_steps_and_direction(current_x, 0)
    move_motor(X_STEP, X_DIR, steps, direction)
    time.sleep(steps * 0.002)

    steps, direction = calculate_steps_and_direction(current_y, 0)
    move_motor(Y_STEP, Y_DIR, steps, direction)
    time.sleep(steps * 0.002)

    steps, direction = calculate_steps_and_direction(current_z, 0)
    move_motor(Z_STEP, Z_DIR, steps, direction)
    time.sleep(steps * 0.002)
    print("Arrived original, program finish")
finally:
    GPIO.cleanup()

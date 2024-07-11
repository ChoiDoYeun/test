import RPi.GPIO as GPIO
import time

# 모터 드라이버 핀 설정
X_STEP = 17
X_DIR = 18
Y_STEP = 27
Y_DIR = 22
Z_STEP_1 = 23
Z_DIR_1 = 24
Z_STEP_2 = 25
Z_DIR_2 = 8
A_STEP = 10  # A모터 핀설정
A_DIR = 9
LIMIT_X = 5
LIMIT_Y = 6
LIMIT_Z = 16


# 스텝 설정
STEPS_PER_MM = 200  # 1mm당 필요한 스텝 수

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup([X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2, A_STEP, A_DIR], GPIO.OUT)
GPIO.setup([LIMIT_X, LIMIT_Y, LIMIT_Z], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 현재위치 초기화
current_x = 0
current_y = 0
current_z = 0

# 모터 동작 함수
def move_motor(step_pin, dir_pin, steps, direction):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.0002)  # 
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.0002)

def move_Z_motor(step1_pin, dir1_pin, step2_pin, dir2_pin, steps, direction):
    GPIO.output(dir1_pin, direction)
    GPIO.output(dir2_pin, direction)
    
    for _ in range(steps):
        GPIO.output(step1_pin, GPIO.HIGH)
        GPIO.output(step2_pin, GPIO.HIGH)
        time.sleep(0.0002)  # 0.0002
        GPIO.output(step1_pin, GPIO.LOW)
        GPIO.output(step2_pin, GPIO.LOW)
        time.sleep(0.0002)

# dir, step 계산 함수
def calculate_steps_and_direction(current_pos, target_pos):
    if target_pos > current_pos:
        direction = GPIO.HIGH
        steps = (target_pos - current_pos) * STEPS_PER_MM
    else:
        direction = GPIO.LOW
        steps = (current_pos - target_pos) * STEPS_PER_MM
    return steps, direction
        
# 리밋 스위치 동작 함수
def move_origin(y_step, y_dir, x_step, x_dir, step1_pin, step2_pin, dir1_pin, dir2_pin):

   while LIMIT_Y == True:
      move_motor(y_step, y_dir, 1, GPIO.LOW)
      current_y = origin.y
   time.sleep(0.01)
    
   while LIMIT_X == True:
      move_motor(x_step, x_dir, 1, GPIO.LOW)
      current_x = origin.x
   time.sleep(0.01)
   
   while LIMIT_Z == True:
      move_Z_motor(step1_pin, dir1_pin, step2_pin, dir2_pin, 1, GPIO.LOW)
      current_z = origin.z
   time.sleep(0.01)

try:
    while True:

        if GPIO.input(LIMIT_Y) == GPIO.LOW:
            print("move y")
        
        elif GPIO.input(LIMIT_X) == GPIO.LOW:
            print("move x")
        
        elif GPIO.input(LIMIT_Z) == GPIO.LOW:
            print("move z")
        
        else : 
            print("nothing input")
            time.sleep(0.5)
        #print("z check")

        # target_x = 87
        # target_y = 85
        # target_z = 224

        # # Z축 이동
        # steps, direction = calculate_steps_and_direction(current_z, target_z) # Z축 dir방향, step수 계산
        # move_Z_motor(Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2, steps, direction) # Z축 모터 동작
        # time.sleep(0.002)  # 대기 시간
        # current_z = target_z  # 현재 Z 위치 업데이트

        # # X축 이동
        # steps, direction = calculate_steps_and_direction(current_x, target_x) # X축 dir방향, step수 계산
        # move_motor(X_STEP, X_DIR, steps, direction) # X축 모터 동작
        # time.sleep(0.002)  # 대기 시간
        # current_x = target_x  # 현재 X 위치 업데이트

        # # Y축 이동
        # steps, direction = calculate_steps_and_direction(current_y, target_y) # Y축 dir방향, step수 계산
        # move_motor(Y_STEP, Y_DIR, steps, direction) # Y축 모터 동작
        # print(direction)
        # time.sleep(0.002)  # 대기 시간
        # current_y = target_y  # 현재 Y 위치 업데이트

        # time.sleep(1)

        # move_origin(y_step, y_dir, x_step, x_dir, step1_pin, step2_pin, dir1_pin, dir2_pin)

        # time.sleep(1)        # target_x = 87
        # target_y = 85
        # target_z = 224

        # # Z축 이동
        # steps, direction = calculate_steps_and_direction(current_z, target_z) # Z축 dir방향, step수 계산
        # move_Z_motor(Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2, steps, direction) # Z축 모터 동작
        # time.sleep(0.002)  # 대기 시간
        # current_z = target_z  # 현재 Z 위치 업데이트

        # # X축 이동
        # steps, direction = calculate_steps_and_direction(current_x, target_x) # X축 dir방향, step수 계산
        # move_motor(X_STEP, X_DIR, steps, direction) # X축 모터 동작
        # time.sleep(0.002)  # 대기 시간
        # current_x = target_x  # 현재 X 위치 업데이트

        # # Y축 이동
        # steps, direction = calculate_steps_and_direction(current_y, target_y) # Y축 dir방향, step수 계산
        # move_motor(Y_STEP, Y_DIR, steps, direction) # Y축 모터 동작
        # print(direction)
        # time.sleep(0.002)  # 대기 시간
        # current_y = target_y  # 현재 Y 위치 업데이트

        # time.sleep(1)

        # move_origin(y_step, y_dir, x_step, x_dir, step1_pin, step2_pin, dir1_pin, dir2_pin)

        # time.sleep(1)
        
except KeyboardInterrupt: #추후 stop버튼 푸쉬시 동작하도록 변경해야함
    print("Before finish, should move to original. plz wait")
    # 현재 위치에서 (0,0,0)으로 이동
    steps, direction = calculate_steps_and_direction(current_x, 0)
    move_motor(X_STEP, X_DIR, steps, direction)
    time.sleep(0.002)  # 대기 시간

    steps, direction = calculate_steps_and_direction(current_y, 0)
    move_motor(Y_STEP, Y_DIR, steps, direction)
    time.sleep(0.002)  # 대기 시간

    steps, direction = calculate_steps_and_direction(current_z, 0)
    move_Z_motor(Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2, steps, direction) # Z축 모터 동작
    time.sleep(0.002)  # 대기 시간
    print("Arrived original, program finish")
    
finally:
    GPIO.cleanup()

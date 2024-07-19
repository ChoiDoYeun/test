import RPi.GPIO as GPIO
import time

# 모터 드라이버 핀 설정
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
LIMIT_Y = 19
LIMIT_Z = 16

Con_STEP = 7
Con_DIR = 13


# 스텝 설정
STEPS_PER_MM = 200  # 1mm당 필요한 스텝 수

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup([X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2, A_STEP, A_DIR,Con_STEP,Con_DIR], GPIO.OUT)
GPIO.setup([LIMIT_X, LIMIT_Y, LIMIT_Z], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 현재위치 초기화
current_x = 0
current_y = 0
current_z = 0

origin_x = 0
origin_y = 0
origin_z = 0

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
        
try:
    while True:

        target_x = int(input("target X : "))
        target_y = int(input("target Y : "))
        target_z = int(input("target Z : "))

        # Z축 이동
        steps, direction = calculate_steps_and_direction(current_z, target_z) # Z축 dir방향, step수 계산
        move_Z_motor(Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2, steps, direction) # Z축 모터 동작
        time.sleep(0.002)  # 대기 시간
        current_z = target_z  # 현재 Z 위치 업데이트

        # X축 이동
        steps, direction = calculate_steps_and_direction(current_x, target_x) # X축 dir방향, step수 계산
        move_motor(X_STEP, X_DIR, steps, direction) # X축 모터 동작
        time.sleep(0.002)  # 대기 시간
        current_x = target_x  # 현재 X 위치 업데이트

        # Y축 이동
        steps, direction = calculate_steps_and_direction(current_y, target_y) # Y축 dir방향, step수 계산
        move_motor(Y_STEP, Y_DIR, steps, direction) # Y축 모터 동작
        time.sleep(0.002)  # 대기 시간
        current_y = target_y  # 현재 Y 위치 업데이트

        time.sleep(2)
        #print(current_x,current_y,current_z)

        print(GPIO.input(LIMIT_Y))

        while GPIO.input(LIMIT_Y) == GPIO.HIGH:
            move_motor(Y_STEP, Y_DIR, 1, GPIO.LOW)
            #print("y move")
            time.sleep(0.0002)
            print(GPIO.input(LIMIT_Y))
            print("   "+str(GPIO.HIGH))
            current_y = origin_y
        print("y done")
        time.sleep(0.1)
        while GPIO.input(LIMIT_X) == GPIO.HIGH:
            move_motor(X_STEP, X_DIR, 1, GPIO.LOW)
            current_x = origin_x
        print("x done")
        time.sleep(0.1)
        
        while GPIO.input(LIMIT_Z) == GPIO.HIGH:
            move_Z_motor(Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2, 1, GPIO.LOW)
            current_z = origin_z

        print("z done")
        time.sleep(0.1)
        print("done origin")

        break
        
except KeyboardInterrupt: #추후 stop버튼 푸쉬시 동작하도록 변경해야함
    print("Before finish, should move to original. plz wait")
    move_origin(Y_STEP,Y_DIR,X_STEP,X_DIR,Z_STEP_1,Z_DIR_1,Z_STEP_2,Z_DIR_2)
    print("done origin")
    
finally:
    GPIO.cleanup()

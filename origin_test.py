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

Con_STEP = 7
Con_DIR = 1

# 스텝 설정
STEPS_PER_MM = 200  # 1mm당 필요한 스텝 수

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup([X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1,Z_STEP_2,Z_DIR_2,A_STEP,A_DIR,Con_STEP,Con_DIR,LIMIT_X,LIMIT_Y,LIMIT_Z], GPIO.OUT)

# 현재위치 초기화
current_x = 0
current_y = 0
current_z = 0
current_a = 0
current_con = 0

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

def move_A_motor(step_pin, dir_pin, steps, direction):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.01)  # 1ms 대기
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.01)

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
def move_origin(x_step,x_dir,step1_pin,step2_pin,dir1_pin,dir2_pin,y_step,y_dir):
   global current_x, current_y, current_z
   X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1,Z_STEP_2,Z_DIR_2,A_STEP,A_DIR,LIMIT_X,LIMIT_Y,LIMIT_Z  = initialize()

   while LIMIT_X == true:
      move_motor(x_step,x_dir,1,GPIO.HIGH)
      current_x = origin.x
   time.sleep(0.01)
   
   while LIMIT_Z == true:
      move_Z_motor(step1_pin, dir1_pin, step2_pin, dir2_pin,1,GPIO.HIGH)
      current_z = origin.z
   time.sleep(0.01)
   
   while LIMIT_Y == true:
      move_motor(y_step,y_dir,1,GPIO.HIGH)
      current_y = origin.y
   time.sleep(0.01)

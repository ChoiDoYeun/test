# 조건
# steps/rev = 400
# microsteps = 2
# screw pitch = 2mm

# step/mm = (steps/rev * microsteps) / screw pitch
#         = (400 * 2) / 2
#         = 400 step/mm
# 스텝수 제어
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

def move_motor(step_pin, dir_pin, steps, direction):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.001)  # 1ms 대기
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.001)

try:
    # 목표 좌표로 이동 ex : (X:100mm, Y:200mm, Z:100mm)
    move_motor(X_STEP, X_DIR, 100 * STEPS_PER_MM, GPIO.HIGH)  # X축 이동
    time.sleep(100 * STEPS_PER_MM * 0.002 + 100)  # Y축 이동에 필요한 시간
    
    move_motor(Y_STEP, Y_DIR, 200 * STEPS_PER_MM, GPIO.HIGH)  # Y축 이동
    time.sleep(200 * STEPS_PER_MM * 0.002 + 100)  # Y축 이동에 필요한 시간
    
    move_motor(Z_STEP, Z_DIR, 100 * STEPS_PER_MM, GPIO.HIGH)  # Z축 이동
finally:
    GPIO.cleanup()

# 드라이버 모듈로 xyz DC모터 제어 예시코드
import RPi.GPIO as GPIO
import time

# 모터 드라이버 핀 설정
X_STEP = 11  # X축 STEP 핀 번호
X_DIR = 12  # X축 DIR 핀 번호
Y_STEP = 27  # Y축 STEP 핀 번호
Y_DIR = 22   # Y축 DIR 핀 번호
Z_STEP = 23  # Z축 STEP 핀 번호
Z_DIR = 24   # Z축 DIR 핀 번호

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(X_STEP, GPIO.OUT)
GPIO.setup(X_DIR, GPIO.OUT)
GPIO.setup(Y_STEP, GPIO.OUT)
GPIO.setup(Y_DIR, GPIO.OUT)
GPIO.setup(Z_STEP, GPIO.OUT)
GPIO.setup(Z_DIR, GPIO.OUT)

# 각 축별로 움직임 함수 정의
def move_motor(step_pin, dir_pin, steps, direction, delay):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)

# 모터 움직임 예제
try:
    move_motor(X_STEP, X_DIR, 200, True, 0.005)  # X축으로 200 스텝
    move_motor(Y_STEP, Y_DIR, 200, True, 0.005)  # Y축으로 200 스텝
    move_motor(Z_STEP, Z_DIR, 200, True, 0.005)  # Z축으로 200 스텝
finally:
    GPIO.cleanup()  # GPIO 핀 초기화

# config.py
import RPi.GPIO as GPIO

STEPS_PER_MM = 200

# Global position variables
current_x = 0
current_y = 0
current_z = 0



def initialize():
    global current_x, current_y, current_z
    X_STEP = 17
    X_DIR = 18
    Y_STEP = 27
    Y_DIR = 22
    Z_STEP_1 = 23
    Z_DIR_1 = 24
    Z_STEP_2 = 25
    Z_DIR_2 = 28
    A_STEP = 10  # A모터 핀설정
    A_DIR = 9
    # GPIO 설정
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1,Z_STEP_2,Z_DIR_2,A_STEP,A_DIR], GPIO.OUT)
    return X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1,Z_STEP_2,Z_DIR_2,A_STEP,A_DIR

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
    Z_STEP = 23
    Z_DIR = 24
    # GPIO 설정
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP, Z_DIR], GPIO.OUT)
    return X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP, Z_DIR

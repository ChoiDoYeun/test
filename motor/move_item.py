# move_item.py
# A 모터 동작
# Con 모터 동작
from motor.move_motor import move_motor, move_A_motor
from motor.config import initialize
import RPi.GPIO as GPIO

def move_item_high():
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1,Z_STEP_2,Z_DIR_2,A_STEP,A_DIR,Con_STEP,Con_DIR,LIMIT_X,LIMIT_Y,LIMIT_Z  = initialize()
    steps = 500 # 예시
    direction = GPIO.HIGH # 예시
    print("A모터 동작중")
    move_A_motor(A_STEP, A_DIR, steps, direction)
    print("A모터 동작완료")
    
def move_item_low():
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1,Z_STEP_2,Z_DIR_2,A_STEP,A_DIR,Con_STEP,Con_DIR,LIMIT_X,LIMIT_Y,LIMIT_Z  = initialize()
    steps = 500 # 예시
    direction = GPIO.LOW # 예시
    print("A모터 동작중")
    move_A_motor(A_STEP, A_DIR, steps, direction)
    print("A모터 동작완료")

def move_con_high():
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1,Z_STEP_2,Z_DIR_2,A_STEP,A_DIR,Con_STEP,Con_DIR,LIMIT_X,LIMIT_Y,LIMIT_Z  = initialize()
    steps = 190
    direction = GPIO.HIGH # 예시
    print("con 동작중")
    move_A_motor(Con_STEP, Con_DIR, steps, direction)
    print("con 동작완료")

def move_con_low():
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1,Z_STEP_2,Z_DIR_2,A_STEP,A_DIR,Con_STEP,Con_DIR,LIMIT_X,LIMIT_Y,LIMIT_Z  = initialize()
    steps = 190
    direction = GPIO.LOW # 예시
    print("con 동작중")
    move_A_motor(Con_STEP, Con_DIR, steps, direction)
    print("con 동작완료")

# move_item.py
# A 모터 동작
from motor.move_motor import move_motor
from motor.config import initialize

def move_item_high():
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP, Z_DIR, A_STEP,A_DIR  = initialize()
    steps = 500 # 예시
    direction = "HIGH" # 예시
    print("A모터 동작중")
    move_motor(A_STEP, A_DIR, steps, direction)
    print("A모터 동작완료")
    
def move_item_low():
    X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP, Z_DIR, A_STEP,A_DIR  = initialize()
    steps = 500 # 예시
    direction = "LOW" # 예시
    print("A모터 동작중")
    move_motor(A_STEP, A_DIR, steps, direction)
    print("A모터 동작완료")

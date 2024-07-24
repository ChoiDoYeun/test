from warehouse_class import Warehouse
from motor.move_position import move_position_go,move_position_back
from motor.move_item import move_item_high,move_item_low,move_con_high,move_con_low
from motor.move_origin import move_origin
from motor.in_out_mode import input_mode,output_mode
import time
import RPi.GPIO as GPIO

try:
    while True:

        x = int(input("target X : "))
        y = int(input("target Y : "))
        z = int(input("target Z : "))

        input_mode(x, y, z)

        break
        
except KeyboardInterrupt: #추후 stop버튼 푸쉬시 동작하도록 변경해야함
    print("Before finish, should move to original. plz wait")
    move_origin(Y_STEP,Y_DIR,X_STEP,X_DIR,Z_STEP_1,Z_DIR_1,Z_STEP_2,Z_DIR_2)
    print("done origin")
    
finally:
    GPIO.cleanup()

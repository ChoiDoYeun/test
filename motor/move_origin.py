import RPi.GPIO as GPIO
import time
from motor.config import initialize, current_x, current_y, current_z,origin_x,origin_y,origin_z
from motor.move_motor import move_motor, move_Z_motor

def move_origin(Y_STEP, Y_DIR, X_STEP, X_DIR, Z_STEP_1, Z_DIR_1, Z_STEP_2, Z_DIR_2, LIMIT_X, LIMIT_Y, LIMIT_Z):
   global current_x, current_y, current_z,origin_x,origin_y,origin_z
   while GPIO.input(LIMIT_Y) == GPIO.HIGH:
      move_motor(Y_STEP, Y_DIR, 1, GPIO.LOW)
      time.sleep(0.0002)
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
   



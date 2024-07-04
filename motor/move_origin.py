import RPi.GPIO as GPIO
import time
from motor.config import initialize, current_x, current_y, current_z
from motor.move_motor import move_motor, move_Z_motor

def move_origin(x_step,x_dir,step1_pin,step2_pin,dir1_pin,dir2_pin,y_step,y_dir):
   global current_x, current_y, current_z
   X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP_1, Z_DIR_1,Z_STEP_2,Z_DIR_2,A_STEP,A_DIR,limit_x_switch,limit_y_switch,limit_z_switch  = initialize()

   while limit_x_switch == true:
      move_motor(x_step,x_dir,1,GPIO.HIGH)
      current_x = origin.x
   time.sleep(0.01)
   
   while limit_z_switch == true:
      move_Z_motor(step1_pin, dir1_pin, step2_pin, dir2_pin,1,GPIO.HIGH)
      current_z = origin.z
   time.sleep(0.01)
   
   while limit_y_switch == true:
      move_motor(y_step,y_dir,1,GPIO.HIGH)
      current_y = origin.y
   time.sleep(0.01)

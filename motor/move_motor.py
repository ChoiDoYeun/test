import RPi.GPIO as GPIO
import time

def move_motor(step_pin, dir_pin, steps, direction):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.00025)  # 1ms 대기
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.00025)

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

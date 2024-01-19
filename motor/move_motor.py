import RPi.GPIO as GPIO
import time

def move_motor(step_pin, dir_pin, steps, direction):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.00025)  # 1ms 대기
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.00025)
# calculate_steps_and_direction.py
from motor.config import STEPS_PER_MM
import RPi.GPIO as GPIO

def calculate_steps_and_direction(current_pos, target_pos):
    print(f"현재 위치: {current_pos}, 목표 위치: {target_pos}")
    if target_pos > current_pos:
        direction = GPIO.HIGH
        steps = (target_pos - current_pos) * STEPS_PER_MM
    else:
        direction = GPIO.LOW
        steps = (current_pos - target_pos) * STEPS_PER_MM
    return steps, direction
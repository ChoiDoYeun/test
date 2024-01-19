import RPi.GPIO as GPIO

def initialize():
  # 모터 드라이버 핀 설정
  X_STEP = 17  # X축 STEP 핀 번호
  X_DIR = 18   # X축 DIR 핀 번호
  Y_STEP = 27  # Y축 STEP 핀 번호
  Y_DIR = 22   # Y축 DIR 핀 번호
  Z_STEP = 23  # Z축 STEP 핀 번호
  Z_DIR = 24   # Z축 DIR 핀 번호
  
  # 스텝 설정
  STEPS_PER_MM = 200  # 1mm당 필요한 스텝 수
  
  # GPIO 설정
  GPIO.setmode(GPIO.BCM)
  GPIO.setup([X_STEP, X_DIR, Y_STEP, Y_DIR, Z_STEP, Z_DIR], GPIO.OUT)
  
  # 현재위치 초기화
  current_x = 0
  current_y = 0
  current_z = 0

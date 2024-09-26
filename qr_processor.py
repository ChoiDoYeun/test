# qr_processor.py
import time
from camera import read_qr_code,capture_image
from motor.in_out_mode import input_mode,output_mode
import os

stop_thread = False
class StopThreadException(Exception):
    """커스텀 예외 클래스로 스레드 종료를 위해 사용됩니다."""
    pass

# qr코드 정보처리
def process_qr_code_input(warehouse):
    while True:
        try:
            print("qr 코드 감지중")
            qr_code_image_path = '/home/dodo/test/resize_test.png'
            qr_data = capture_image(qr_code_image_path)
            print("qr 코드 감지완료")
            os.remove(qr_code_image_path)
            os.remove('/home/dodo/test/cropped_test.png')

            if qr_data:
                # QR 코드에서 차량 정보 추출
                car = qr_data.strip()
                if car:
                    # 창고에 차량 정보 저장
                    location = warehouse.store_item(car)
                    if location:
                        print(f"{car}가 {location}에 저장되었습니다.")
                        # 저장 위치의 좌표 계산
                        x, y, z = warehouse.calculate_coordinates(location)
                        # 좌표 입력 모드 호출
                        input_mode(x, y, z)
                    else:
                        print(f"{car}를 저장할 공간이 없습니다.")
                else:
                    print("차량 정보가 QR 코드에 포함되어 있지 않습니다.")
            else:
                print("QR 코드를 읽을 수 없습니다.")
            
            # 0.5초마다 동작
            time.sleep(0.5) # 변경점
        except StopThreadException:
            break  # 예외가 발생하면 루프를 종료합니다.
        
def process_qr_code_output(warehouse):
    while True:
        try:
            print("qr 코드 감지중")
            qr_code_image_path = '/home/dodo/test/resize_test.png'
            qr_data = capture_image(qr_code_image_path)
            print("qr 코드 감지완료")
            if qr_data:
                cars = qr_data.split(',')
                for car in cars:
                    if car:
                        location = warehouse.find_item(car)
                        if location:
                            print(f"{car}가 {location}에서 꺼내집니다.")
                            x, y, z = warehouse.calculate_coordinates(location)
                            output_mode(x, y, z)
                            warehouse.remove_item(location)  # 차량 제거
                        else:
                            print(f"{car}는 창고에 존재하지 않습니다.")
                            
            else:
                print("QR 코드를 읽을 수 없습니다.")
            # 0.5초마다 동작   
            time.sleep(0.5) #변경점
        except StopThreadException:
            break


def process_qr_code(warehouse,state):
    while True:
        try:
            print("qr 코드 감지중")
            qr_code_image_path = '/home/dodo/test/resize_test.png'
            qr_data = capture_image(qr_code_image_path)
            print("qr 코드 감지완료")
            os.remove(qr_code_image_path)
            os.remove('/home/dodo/test/cropped_test.png')
            if state == 'input':
                if qr_data:
                    # QR 코드에서 차량 정보 추출
                    car = qr_data.strip()
                    if car:
                        # 창고에 차량 정보 저장
                        location = warehouse.store_item(car)
                        if location:
                            print(f"{car}가 {location}에 저장되었습니다.")
                            # 저장 위치의 좌표 계산
                            x, y, z = warehouse.calculate_coordinates(location)
                            # 좌표 입력 모드 호출
                            input_mode(x, y, z)
                        else:
                            print(f"{car}를 저장할 공간이 없습니다.")
                    else:
                        print("차량 정보가 QR 코드에 포함되어 있지 않습니다.")
                else:
                    print("QR 코드를 읽을 수 없습니다.")

            elif state == 'output':
                if qr_data:
                    cars = qr_data.split(',')
                    for car in cars:
                        if car:
                            location = warehouse.find_item(car)
                            if location:
                                print(f"{car}가 {location}에서 꺼내집니다.")
                                x, y, z = warehouse.calculate_coordinates(location)
                                output_mode(x, y, z)
                                warehouse.remove_item(location)  # 차량 제거
                            else:
                                print(f"{car}는 창고에 존재하지 않습니다.")
                                
                else:
                    print("QR 코드를 읽을 수 없습니다.")
                    
            else:
                print("대기중")
                
        except StopThreadException:
            break

# qr_processor.py
import time
from camera import read_qr_code,capture_image
from motor.in_out_mode import input_mode,output_mode

stop_thread = False
class StopThreadException(Exception):
    """커스텀 예외 클래스로 스레드 종료를 위해 사용됩니다."""
    pass

# qr코드 정보처리
def process_qr_code_input(warehouse):
    while True:
        try:
            #capture_image(qr_code_image_path)
            qr_code_image_path = '세단_QR_Code.PNG'
            qr_data = read_qr_code(qr_code_image_path)
            if qr_data:
                cars = qr_data.split('\n')
                for car in cars:
                    if car:
                        location = warehouse.store_item(car)
                        if location:
                            print(f"{car}가 {location}에 저장되었습니다.")
                            x, y, z = warehouse.calculate_coordinates(location)
                            input_mode(x,y,z)
                        else:
                            print(f"{car}를 저장할 공간이 없습니다.")
            else:
                print("QR 코드를 읽을 수 없습니다.")
                        # 15초마다 동작
            time.sleep(5)
        except StopThreadException:
            break  # 예외가 발생하면 루프를 종료합니다.
        
def process_qr_code_output(warehouse):
    while True:
        try:
            qr_code_image_path = 'output_qrcode.PNG'
            qr_data = read_qr_code(qr_code_image_path)
            if qr_data:
                cars = qr_data.split('\n')
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
            time.sleep(5)
        except StopThreadException:
            break
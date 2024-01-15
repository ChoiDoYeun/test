import time
from warehouse import Warehouse
from camera_gui import capture_image, read_qr_code
from gui import create_gui

def main():
    warehouse = Warehouse()
    existing_items = {'A12': '차량1', 'A21': '차량2', 'A31': '차량3'}
    warehouse.load_existing_items(existing_items)

    qr_code_image_path = 'captured_image.jpg'

    while True:
        capture_image(qr_code_image_path)
        qr_data = read_qr_code(qr_code_image_path)

        if qr_data:
            cars = qr_data.split('\n')
            for car in cars:
                if car:
                    location = warehouse.store_item(car)
                    if location:
                        print(f"{car}가 {location}에 저장되었습니다.")
                    else:
                        print(f"{car}를 저장할 공간이 없습니다.")
        else:
            print("QR 코드를 읽을 수 없습니다.")

        time.sleep(2)  # Adjust the delay as needed

        create_gui(warehouse)

if __name__ == "__main__":
    main()

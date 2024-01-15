# Let's integrate and modify the provided code to work on a Raspberry Pi.
# The goal is to use the camera.py functionality within the main.py, while ensuring GUI compatibility and performance optimization.

# main.py
import tkinter as tk
import subprocess
from PIL import Image
from pyzbar.pyzbar import decode
import time

# Warehouse class is now a separate module to avoid duplication and can be imported in both camera.py and gui.py
class Warehouse:
    def __init__(self):
        self.storage = {f'{building}{floor}{room}': None for building in 'ABCD' for floor in range(1, 5) for room in range(1, 3)}

    def load_existing_items(self, existing_items):
        for location, item in existing_items.items():
            if location in self.storage:
                self.storage[location] = item

    def store_item(self, item):
        for location in self.storage:
            if not self.storage[location]:
                self.storage[location] = item
                return location
        return None

# Camera functionality integrated into the main application
def capture_image(image_path='captured_image.jpg'):
    subprocess.run(['libcamera-still', '-o', image_path])

def read_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    return decoded_objects[0].data.decode() if decoded_objects else ""

# GUI setup
def create_gui(warehouse):
    root = tk.Tk()
    root.title("Warehouse Management System")
# 현재 창고 위치 섹션
    warehouse_frame = tk.LabelFrame(root, text="CURRENT WAREHOUSE POSITION")
    warehouse_frame.grid(row=0, column=0, padx=10, pady=10)

    for i, building in enumerate(['A', 'B', 'C', 'D']):
        frame = tk.Frame(warehouse_frame, bd=2, relief='sunken')
        frame.grid(row=i//2, column=i%2, padx=5, pady=5)
        for floor in reversed(range(1, 4)):
            for room in range(1, 3):
                location = f'{building}{floor}{room}'
                label_text = warehouse.storage[location] if warehouse.storage[location] else ' '
                label = tk.Label(frame, text=label_text, borderwidth=1, relief="solid", width=10, height=5)
                label.grid(row=3-floor, column=room-1, padx=5, pady=5)
        label = tk.Label(frame, text=building, font=("Arial", 16), width=5, height=2)
        label.grid(row=3, column=0, columnspan=2, pady=5)
# 원하는 영역 선택 섹션
    choose_frame = tk.LabelFrame(root, text="CHOOSE WHAT U WANNA PICK AREA")
    choose_frame.grid(row=0, column=1, padx=10, pady=10)

    button_texts = [
        'A11', 'A12', 'B11', 'B12',
        'A21', 'A22', 'B21', 'B22',
        'A31', 'A32', 'B31', 'B32',
        'C11', 'C12', 'D11', 'D12',
        'C21', 'C22', 'D21', 'D22',
        'C31', 'C32', 'D31', 'D32'
    ]

    for i in range(6):
        for j in range(4):
            button_text = button_texts[i*4+j]
            tk.Button(choose_frame, text=button_text, width=10, height=5).grid(row=i, column=j, padx=5, pady=5)

    # 모드 선택 섹션
    mode_frame = tk.Frame(root)
    mode_frame.grid(row=0, column=2, padx=10, pady=10)

    tk.Button(mode_frame, text="INPUT", width=10, height=5).pack(padx=5, pady=5)
    tk.Button(mode_frame, text="OUTPUT", width=10, height=5).pack(padx=5, pady=5)

    # 실행 및 중지 버튼 섹션
    control_frame = tk.Frame(root)
    control_frame.grid(row=1, column=1, padx=10, pady=10)

    def run():
        print("Run")

    def stop():
        print("Stop")

    tk.Button(control_frame, text="RUN", bg="green", command=run, width=10, height=5).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(control_frame, text="STOP", bg="red", command=stop, width=10, height=5).pack(side=tk.RIGHT, padx=5, pady=5)
    root.mainloop()

def main():
    warehouse = Warehouse()
    existing_items = {
        'A12': '차량1',
        'A21': '차량2',
        'A31': '차량3'
    }
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

        time.sleep(2)  # Adjust the delay as needed for performance optimization

        # Initialize GUI
        create_gui(warehouse)

if __name__ == "__main__":
    main()

# This integrated script is a starting point. Additional modifications may be needed based on the specific Raspberry Pi model and hardware setup.

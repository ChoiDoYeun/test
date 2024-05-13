#gui.py
import tkinter as tk
from controls.button_clicked import button_clicked
from controls.run import run
from controls.stop import stop
from controls.toggle_mode import input_on,input_off,output_off,output_on
from controls.update_labels import update_warehouse_labels

def create_gui(warehouse, callback=None):
    root = tk.Tk()
    root.title("Warehouse Management System")
    root.geometry("750x480")  # 해상도

    # 창고 위치 레이블 관리를 위한 딕셔너리
    warehouse_labels = {}

    # 현재 창고 위치 섹션
    warehouse_frame = tk.LabelFrame(root, text="CURRENT WAREHOUSE POSITION")
    warehouse_frame.grid(row=0, column=0, padx=5, pady=5)

    for i, building in enumerate(['A', 'B', 'C', 'D']):
        frame = tk.Frame(warehouse_frame, bd=2, relief='sunken')
        frame.grid(row=0, column=i, padx=5, pady=5)  # 모든 프레임을 한 행에 나열
        for floor in reversed(range(1, 4)):
            for room in range(1, 3):
                location = f'{building}{floor}{room}'
                label_text = warehouse.storage[location] if warehouse.storage[location] else ' '
                label = tk.Label(frame, text=label_text, font=("Arial", 8),borderwidth=1, relief="solid", width=8, height=3)
                label.grid(row=3-floor, column=room-1, padx=5, pady=5)
                # 레이블을 딕셔너리에 저장
                warehouse_labels[location] = label

        label = tk.Label(frame, text=building, font=("Arial", 12), width=2, height=2)
        label.grid(row=3, column=0, columnspan=2, pady=5)

    # 업데이트 함수 호출
    update_warehouse_labels(root, warehouse, warehouse_labels)
    
# # 원하는 영역 선택 섹션
#     choose_frame = tk.LabelFrame(root, text="CHOOSE WHAT U WANNA PICK AREA")
#     choose_frame.grid(row=0, column=1, padx=10, pady=10)        

#     button_texts = [
#         'A11', 'A12', 'B11', 'B12',
#         'A21', 'A22', 'B21', 'B22',
#         'A31', 'A32', 'B31', 'B32',
#         'C11', 'C12', 'D11', 'D12',
#         'C21', 'C22', 'D21', 'D22',
#         'C31', 'C32', 'D31', 'D32'
#     ]

#     for i in range(6):
#         for j in range(4):
#             button_text = button_texts[i*4+j]
#             button = tk.Button(choose_frame, text=button_text, width=10, height=5,command=lambda bt=button_text: callback(bt, root, warehouse, warehouse_labels) if callback else None)
#             button.grid(row=i, column=j, padx=5, pady=5)

    # 모드 선택 섹션
    mode_frame = tk.Frame(root)
    mode_frame.grid(row=0, column=1, padx=2, pady=2, sticky='w')

    input_on_button = tk.Button(mode_frame, text="INPUT ON", width=10, height=3, command=lambda: input_on(warehouse))
    input_on_button.grid(row=0, column=0, padx=2, pady=2)  # grid를 사용하여 버튼 위치 지정

    input_off_button = tk.Button(mode_frame, text="INPUT OFF", width=10, height=3, command=input_off)
    input_off_button.grid(row=1, column=0, padx=2, pady=2)  # 나란히 배치

    output_on_button = tk.Button(mode_frame, text="OUTPUT ON", width=10, height=3, command=lambda: output_on(warehouse))
    output_on_button.grid(row=2, column=0, padx=2, pady=2)

    output_off_button = tk.Button(mode_frame, text="OUTPUT OFF", width=10, height=3, command=output_off)
    output_off_button.grid(row=3, column=0, padx=2, pady=2)

    # 실행 및 중지 버튼 섹션
    control_frame = tk.Frame(root)
    control_frame.grid(row=1, column=1, padx=10, pady=10, sticky='e')

    tk.Button(control_frame, text="RUN", bg="green", command=lambda: run(warehouse), width=8, height=3).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(control_frame, text="STOP", bg="red", command=stop, width=8, height=3).pack(side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()

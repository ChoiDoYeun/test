#gui.py
import tkinter as tk
from controls.button_clicked import button_clicked
from controls.run import run
from controls.stop import stop
from controls.toggle_mode import toggle_mode

def create_gui(warehouse, callback=None):
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
            button = tk.Button(choose_frame, text=button_text, width=10, height=5,command=lambda bt=button_text: callback(bt) if callback else None)
            button.grid(row=i, column=j, padx=5, pady=5)

    # 모드 선택 섹션
    mode_frame = tk.Frame(root)
    mode_frame.grid(row=0, column=2, padx=10, pady=10)

    # 버튼 상태를 저장할 변수
    input_mode = {'state': False}
    output_mode = {'state': False}


    input_button = tk.Button(mode_frame, text="INPUT", width=10, height=5, command=lambda: toggle_mode(input_button, input_mode, "INPUT"))
    input_button.pack(padx=5, pady=5)

    output_button = tk.Button(mode_frame, text="OUTPUT", width=10, height=5, command=lambda: toggle_mode(output_button, output_mode, "OUTPUT"))
    output_button.pack(padx=5, pady=5)


    # 실행 및 중지 버튼 섹션
    control_frame = tk.Frame(root)
    control_frame.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(control_frame, text="RUN", bg="green", command=run, width=10, height=5).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(control_frame, text="STOP", bg="red", command=stop, width=10, height=5).pack(side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()
import tkinter as tk
from controls.button_clicked import button_clicked
from controls.run import run
from controls.stop import stop
from controls.toggle_mode import input_on, input_off, output_off, output_on
from controls.update_labels import update_warehouse_labels

def create_warehouse_section(root, warehouse, warehouse_labels):
    warehouse_frame = tk.LabelFrame(root, text="CURRENT WAREHOUSE POSITION")
    warehouse_frame.grid(row=0, column=0, padx=5, pady=5)

    for i, building in enumerate(['A', 'B', 'C', 'D']):
        frame = tk.Frame(warehouse_frame, bd=2, relief='sunken')
        frame.grid(row=0, column=i, padx=5, pady=5)
        for floor in reversed(range(1, 4)):
            for room in range(1, 3):
                location = f'{building}{floor}{room}'
                label_text = warehouse.storage[location] if warehouse.storage[location] else ' '
                label = tk.Label(frame, text=label_text, font=("Arial", 8), borderwidth=1, relief="solid", width=10, height=6)
                label.grid(row=3-floor, column=room-1, padx=5, pady=5)
                warehouse_labels[location] = label

        label = tk.Label(frame, text=building, font=("Arial", 12), width=2, height=5)
        label.grid(row=3, column=0, columnspan=2, pady=5)

    update_warehouse_labels(root, warehouse, warehouse_labels)

def create_mode_buttons(root, warehouse):
    mode_frame = tk.Frame(root)
    mode_frame.grid(row=0, column=1, padx=2, pady=2, sticky='w')

    input_on_button = tk.Button(mode_frame, text="INPUT ON", width=10, height=3, command=lambda: input_on(warehouse))
    input_on_button.grid(row=0, column=0, padx=2, pady=2)

    input_off_button = tk.Button(mode_frame, text="INPUT OFF", width=10, height=3, command=input_off)
    input_off_button.grid(row=1, column=0, padx=2, pady=2)

    output_on_button = tk.Button(mode_frame, text="OUTPUT ON", width=10, height=3, command=lambda: output_on(warehouse))
    output_on_button.grid(row=2, column=0, padx=2, pady=2)

    output_off_button = tk.Button(mode_frame, text="OUTPUT OFF", width=10, height=3, command=output_off)
    output_off_button.grid(row=3, column=0, padx=2, pady=2)

    return mode_frame

def create_control_buttons(mode_frame):
    control_frame = tk.Frame(mode_frame)
    control_frame.grid(row=4, column=0, padx=2, pady=2)

    tk.Button(control_frame, text="RUN", bg="green", command=run, width=10, height=3).pack(side=tk.TOP, padx=5, pady=5)

def create_gui(warehouse, callback=None):
    root = tk.Tk()
    root.title("Warehouse Management System")
    root.geometry("750x480")

    warehouse_labels = {}

    create_warehouse_section(root, warehouse, warehouse_labels)
    mode_frame = create_mode_buttons(root, warehouse)
    create_control_buttons(mode_frame)

    root.mainloop()

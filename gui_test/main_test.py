# main_test.py
import camera
import gui
import tkinter as tk

def main():
    warehouse_data = camera.process_data()  # camera.py에서 데이터 처리
    root = tk.Tk()
    root.title("Warehouse Management System")
    gui.create_and_run_gui(root, warehouse_data)  # GUI 생성 및 실행

if __name__ == "__main__":
    main()

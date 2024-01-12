# main_test.py
import camera_gui
import gui

def main():
    # Get the updated warehouse data from camera_gui
    warehouse_data = camera_gui.process_data()
    
    # Create and run the GUI with the warehouse data
    gui.create_gui(warehouse_data)

if __name__ == "__main__":
    main()

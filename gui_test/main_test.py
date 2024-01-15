import threading
from warehouse import Warehouse
from gui import create_gui
from qr_processor import process_qr_code

def main():
    warehouse = Warehouse()
    existing_items = {'A12': '차량1', 'A21': '차량2', 'A31': '차량3'}
    warehouse.load_existing_items(existing_items)

    qr_thread = threading.Thread(target=process_qr_code, args=(warehouse,))
    qr_thread.daemon = True
    qr_thread.start()

    create_gui(warehouse)

if __name__ == "__main__":
    main()

# update_labels.py
# gui의 현 저장상태판 업데이트 함수
def update_warehouse_labels(root, warehouse, warehouse_labels):
    for location, label in warehouse_labels.items():
        label_text = warehouse.storage[location] if warehouse.storage[location] else ' '
        label.config(text=label_text)
    root.after(1000, lambda: update_warehouse_labels(root, warehouse, warehouse_labels))
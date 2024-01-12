# warehouse.py
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

# warehouse.py
class Warehouse:
    def __init__(self):
        self.storage = {f'{building}{floor}{room}': None for building in 'ABCD' for floor in range(1, 4) for room in range(1, 3)}
    
    def load_existing_items(self, existing_items):
        for location, item in existing_items.items():
            if location in self.storage:
                self.storage[location] = item

    def store_item(self, item):
        for location in self.storage:
            if not self.storage[location]:
                self.storage[location] = item
                return location

    # location의 좌표계산 -> target_pos으로 move_motor.py에서 사용될것
    def calculate_coordinates(self, location):
        building = location[0]
        floor = int(location[1])
        room = int(location[2])

        # X좌표 계산 : A&C는 85 ,B&D는 329
        x = 85 if building in ['A', 'C'] else 329
        x += (room - 1) * 76

        # Y 좌표 계산 : 1층 증가할때마다 +85
        y = 0 + (floor - 1) * 85

        # Z 좌표 계산 : A&B는 264,C&D는 504
        z = 264 if building in ['A', 'B'] else 504 

        return x, y, z
    
    def remove_item(self, location):
        print("상태창에서 차량 제거")
        if location in self.storage:
            self.storage[location] = None
            
    def find_item(self, item):
        for location, stored_item in self.storage.items():
            if stored_item == item:
                return location

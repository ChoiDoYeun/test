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

        # X좌표 계산 : A&C는 100 ,B&D는 250
        x = 100 if building in ['A', 'C'] else 250
        x += (room - 1) * 50

        # Y 좌표 계산 : 1층 증가할때마다 +50
        y = 50 + (floor - 1) * 50

        # Z 좌표 계산 : A&B는 80,C&D는 230
        z = 80 if building in ['A', 'B'] else 230 

        return x, y, z
    
    def remove_item(self, location):
        print("상태창에서 차량 제거")
        if location in self.storage:
            self.storage[location] = None
            
    def find_item(self, item):
        for location, stored_item in self.storage.items():
            if stored_item == item:
                return location
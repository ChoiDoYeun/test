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

    def calculate_coordinates(self, location):
        building = location[0]
        floor = int(location[1])
        room = int(location[2])

        # X좌표 계산 : A&C는 100 ,B&D는 250
        x = 100 if building in ['A', 'C'] else 250  # Start at 100 for A and C, 250 for B and D
        x += (room - 1) * 50  # Increase X by 50 for each room

        # Y 좌표 계산 : 1층 증가할때마다 +50
        y = 50 + (floor - 1) * 50

        # Z 좌표 계산 : A&B는 80,C&D는 230
        z = 80 if building in ['A', 'B'] else 230  # 80 for A and B, 230 for C and D

        return x, y, z

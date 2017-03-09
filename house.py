class Room:
    def __init__(self, length, width, windows):
        self.length = length
        self.width = width
        self.windows = windows

    def get_area(self):
        return self.length * self.width

    def get_windows(self):
        return self.windows


class Apartment:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def total_area(self):
        total_area = 0
        for room in self.rooms:
            total_area += room.get_area()
        return total_area

    def total_windows(self):
        total_windows = 0
        for room in self.rooms:
            total_windows += room.get_windows()
        return total_windows

room_1 = Room(10, 10, 2)
room_2 = Room(15, 30, 2)
room_3 = Room(13, 15, 2)

aprart_1 = Apartment()
aprart_1.add_room(room_1)
aprart_1.add_room(room_2)
aprart_1.add_room(room_3)

print(aprart_1.total_area())
print(aprart_1.total_windows())


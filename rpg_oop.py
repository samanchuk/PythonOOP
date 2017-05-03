from threading import Thread
from random import randint


class Room:
    _rooms = []

    def __init__(self, id, title, description, exits):
        self.id = id
        self.title = title
        self.description = description
        self.exits = exits
        self._add_room(self)
        self.room_item_list = []
        self.npc = []

    def __str__(self):
        return 'Room title {0} description {1}'.format(self.title, self.description)

    def __repr__(self):
        return 'Room id:{0} {1} {2}'.format(self.id, self.title, self.description)

    def _add_room(cls, room):
        cls._rooms.append(room)

    _add_room = classmethod(_add_room)

    def get_room_by_id(self, id):
        for room in self._rooms:
            if room.id == id:
                return room

    def print_exits(self):
        for direction in self.exits.keys():
            room = self.get_room_by_id(self.exits.get(direction))
            if room and room.id == self.exits.get(direction):
                print('Exit direction: \n\t{0} \nroom:\n\t{1}'.format(direction, room.description))

    def exits_rooms(self):
        rooms_exits = {}
        for ex in self.exits.keys():
            if self.get_room_by_id(self.exits.get(ex)):
                rooms_exits[ex] = self.get_room_by_id(self.exits.get(ex))
        return rooms_exits


class Character:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.char_item_list = []

    def move_to_room(self, direction):
        if direction in self.room.exits_rooms().keys():
            for direct in self.room.exits_rooms().keys():
                if direct.startswith(direction):
                    self.room = self.room.exits_rooms().get(direct)
                    print(self.room)
                    break
        else:
            print('No such exit')

    def scan_room(self):
        print(self.room)
        for i in self.room.room_item_list:
            print('{0}:\n\t{1}'.format(i.name, i.description))

    def scan_exits(self):
        print('You have following exits:')
        self.room.print_exits()

    def get_item(self, name):
        for i in range(len(self.room.room_item_list)):
            if self.room.room_item_list[i].name.startswith(name):
                self.char_item_list.append(self.room.room_item_list.pop(i))
                break

    def throw_item(self, name):
        for i in range(len(self.char_item_list)):
            if self.char_item_list[i].name.startswith(name):
                self.room.room_item_list.append(self.char_item_list.pop(i))
                break

    def show_char_items(self):
        print('You have:')
        if len(self.char_item_list) == 0:
            print('0 items')
        else:
            for item in self.char_item_list:
                print('{0}'.format(item.name))


class Handlers:
    commands = []

    def get_commands(self):
        for i in self.commands:
            if i[0] and i[-1]:
                print(i[0], i[-1], end=', ')

    def register(self, name, func, arg=None):
        self.commands.append([name, func, arg])

    def unregister(self, name):
        for i in range(len(self.commands)):
            if self.commands[i][0] == name:
                self.commands.pop(i)
                break

    def get_comm(self, name):
        command_sp = name.split()
        for i in range(len(self.commands)):
            if self.commands[i][0].startswith(command_sp[0]) and len(command_sp) == 1:
                return self.commands[i]
            elif self.commands[i][0].startswith(command_sp[0]) and self.commands[i][2].startswith(
                    command_sp[1]) and len(command_sp) > 1:
                return self.commands[i]

    def run(self, command):
        command_name = command.split()
        if self.get_comm(command):
            if len(command_name) == 2 and self.get_comm(command)[2] is not None:
                self.get_comm(command)[1](self.get_comm(command)[2])
            elif command and self.get_comm(command)[2] is not None:
                self.get_comm(command)[1](self.get_comm(command)[2])
            elif self.get_comm(command)[2] is None and len(command_name) < 2:
                self.get_comm(command)[1]()
            else:
                print('Wrong parameter!!!')
        else:
            print('Wrong command!!!')


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Npc(Thread):
    def __init__(self, name, health, hit, room):
        super().__init__()
        self.name = name
        self.health = health
        self.hit = hit
        self.room = room

    def move_to_room(self):
        exits = list(self.room.exits_rooms().keys())
        rand_exit = exits[randint(0, 1)]
        self.room
        return rand_exit

def main():
    handler = Handlers()
    it1 = Item('book', 'on floor')
    it2 = Item('lamp', 'at the window')
    it3 = Item('knife', 'near the door')
    r1 = Room('1', 'room1', 'this is 1 room', {'south': '3', 'east': '2'})
    r2 = Room('2', 'room2', 'this is 2 room', {'south': '4', 'west': '1'})
    r3 = Room('3', 'room3', 'this is 3 room', {'east': '4', 'north': '1'})
    r4 = Room('4', 'room4', 'this is 4 room', {'north': '2', 'west': '3'})
    r1.room_item_list = [it1, it2, it3]
    char = Character('Me', r1)
    handler.register('east', char.move_to_room, 'east')
    handler.register('west', char.move_to_room, 'west')
    handler.register('south', char.move_to_room, 'south')
    handler.register('north', char.move_to_room, 'north')
    handler.register('scan', char.scan_room)
    handler.register('exits', char.scan_exits)
    handler.register('get', char.get_item, 'book')
    handler.register('get', char.get_item, 'lamp')
    handler.register('get', char.get_item, 'knife')
    handler.register('throw', char.throw_item, 'book')
    handler.register('throw', char.throw_item, 'lamp')
    handler.register('throw', char.throw_item, 'knife')
    handler.register('show_items', char.show_char_items)
    while True:
        command = input('Enter command: ')
        if command.startswith('sto'):
            break
        handler.run(command)

r1 = Room('1', 'room1', 'this is 1 room', {'south': '3', 'east': '2'})
r2 = Room('2', 'room2', 'this is 2 room', {'south': '4', 'west': '1'})
r3 = Room('3', 'room3', 'this is 3 room', {'east': '4', 'north': '1'})
r4 = Room('4', 'room4', 'this is 4 room', {'north': '2', 'west': '3'})


ork = Npc('Bolk', 100, 20, r1)
ork.move_to_room()

# main()

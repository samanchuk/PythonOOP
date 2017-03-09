class Car:
    def __init__(self, car_type):
        self.type = car_type

    def get_type(self):
        return self.car_type


class Block:
    def __init__(self, car_type, limit, block_id):
        self.car_type = car_type
        self.limit = limit
        self.block_id = block_id
        self.cars_id_to_car = {}
        self.counter = 0

    def add_car(self, car):
        if self.car_type <= car.get_type():
            car_id = self.block_id + '_' + car + '_' + self.counter
            self.cars_id_to_car = self.block_id[car_id][car]
            self.counter += 1
            return car_id

    def get_car(self, car_id):
        return self.cars_id_to_car[self.block_id][car_id]

    def __str__(self):
        return 'Block ID: {0}, Cars Limit: {1}, Car Type: {2}'.format(self.block_id, self.limit, self.car_type)


class Parking:
    def __init__(self):
        self.blocks_list = []
        self.blocks_id = 0

    def add_block(self, block):
        self.blocks_list.append(block(block_id=self.blocks_id))
        self.blocks_id += 1

    def get_car_from_parking(self, car_id):
        for block in self.blocks_list:
            block.get_car(self.car_id)


p1 = Parking()

p1.add_block(1, 10)
p1.add_block(2, 8, 0)
p1.add_block(3, 5, 0)

car1 = Car(1)

for block in p1.blocks_list:
    block.add_car(car1)

for block in p1.blocks_list:
    print(block)

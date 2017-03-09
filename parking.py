class Car:
    def __init__(self, car_class):
        self.car_class = car_class

    def get_type(self):
        return self.car_class

    def __str__(self):
        return 'This is {0} class auto'.format(self.car_class)


class Block:
    def __init__(self, block_type, capacity):
        self.cars_data = {}
        self.block_type = block_type
        self.capacity = capacity
        self.counter = 0

    def add_car(self, car):
        car_id = str(self.counter) + '_' + str(car.get_type())
        self.cars_data[car_id] = car
        self.counter += 1
        return car_id

    def remove_car(self, car_id):
        return self.cars_data.pop(car_id)

    def info(self):
        for block_car in self.cars_data.keys():
            print('Car ID: {0} {1}'.format(block_car, self.cars_data[block_car]))

    def get_block_type(self):
        return self.block_type

    def get_block_free_places(self):
        return self.capacity - len(self.cars_data.keys())

    def get_car_id(self):
        return list(self.cars_data.keys())


class Parking:
    def __init__(self):
        self.blocks_list = []

    def add_block_to_parking(self, block):
        self.blocks_list.append(block)

    def add_car_to_parking(self, car):
        for block_id in self.blocks_list:
            if car.get_type() <= block_id.get_block_type() and block_id.get_block_free_places() > 0:
                return block_id.add_car(car)

    def remove_car_from_parking(self, car_id):
        for block_id in self.blocks_list:
            if car_id in block_id.get_car_id():
                block_id.remove_car(car_id)

    def get_blocks_info(self):
        for block_id in self.blocks_list:
            block_id.info()


def main():
    car_1 = Car(1)
    car_2 = Car(2)
    car_3 = Car(1)
    block_for_1 = Block(1, 2)
    block_for_2 = Block(2, 2)
    my_parking = Parking()
    my_parking.add_block_to_parking(block_for_1)
    my_parking.add_block_to_parking(block_for_2)
    my_parking.add_car_to_parking(car_1)
    my_parking.add_car_to_parking(car_2)
    my_parking.add_car_to_parking(car_3)
    my_parking.get_blocks_info()
    print('====================')
    my_parking.remove_car_from_parking('0_1')
    my_parking.get_blocks_info()
    
main()

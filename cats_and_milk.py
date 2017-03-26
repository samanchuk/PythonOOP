from threading import Thread
from threading import Lock
from time import sleep
from random import randint


class Cat(Thread):
    def __init__(self, name, plate):
        super().__init__()
        self.name = name
        self.plate = plate

    def run(self):
        while True:
            if self.plate.get_swallows() > 0:
                self.plate.lock.acquire()
                swallows = randint(3, 8)
                self.plate.drink(swallows)
                print('Cat {0} come to drink milk, and drinks {1} swallows'.format(self.name, swallows))
                sleep(randint(1, 10))
                self.plate.lock.release()
                print('{0} swallows left in plate'.format(self.plate.get_swallows()))
                print('Cat {0} goes away'.format(self.name))
            else:
                break


class Girl(Thread):
    def __init__(self, name, plate):
        super().__init__()
        self.name = name
        self.plate = plate

    def run(self):
        while True:
            if self.plate.get_swallows() <= 30:
                self.plate.lock.acquire()
                swallows_fill = randint(10, 15)
                print('{0} fills {1} swallows'.format(self.name, swallows_fill))
                print('There are {0} swallows in plate'.format(self.plate.fill(swallows_fill)))
                sleep(randint(1, 10))
                self.plate.lock.release()
                print('Girl {0} goes away'.format(self.name))
            else:
                pass


class Plate:
    def __init__(self, swallows):
        self.swallows = swallows
        self.lock = Lock()

    def fill(self, swl_amount):
        self.swallows += swl_amount
        return self.swallows

    def drink(self, swl_amount):
        if self.swallows > 0:
            self.swallows -= swl_amount
            return True
        else:
            return False

    def get_swallows(self):
        return self.swallows


plate = Plate(10)

Girl('Dasha', plate).start()
Cat('Murzik', plate).start()
Cat('Barsik', plate).start()
Cat('Fedia', plate).start()

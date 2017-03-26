from threading import Thread
from random import randint
from time import sleep


class Cat(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._alive = True
        self._here = True

    def run(self):
        while self._alive:
            if self._here and randint(1, 10) <= 3:
                print('{0} убежал за тучку!'.format(self.name))
                self._here = False
            elif self._here and randint(1, 10) <= 3:
                print('{0} почесал лапой за ухом'.format(self.name))
            elif not self._here and randint(1, 10) <= 3:
                print('{0} Выглянул из-за тучки!'.format(self.name))
            elif not self._here and randint(1, 10) <= 3:
                print('{0} прибежал из-за тучки'.format(self.name))
                self._here = True
            sleep(randint(4, 6))


class Dog(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        while True:
            for cat in cats:
                if cat._alive and cat._here and randint(1, 10) <= 3:
                    print('Рычим на кота {0}'.format(cat.name))
                elif cat._alive and cat._here and randint(1, 10) <= 3:
                    print('Кусаем кота {0} на смерть'.format(cat.name))
                    cat._alive = False
            sleep(randint(4, 6))


cats = []
cats.append(Cat('Мурзик'))
cats.append(Cat('Барсик'))

[i.start() for i in cats]

dog = Dog('Рекс')
dog.start()
from threading import Thread
from threading import Lock
from time import sleep

data = ['dasas', 'sdasdada', 'dsadadas', 'dasdasdq', 'dsadidow', 'qwyeqruq', 'ri9ypypp', '3247ro595', 'hfkfkhjfhf']
d = Lock()
lst = []
l = Lock()


class Process(Thread):
    def __init__(self, data, num):
        super().__init__()
        self.data = data
        self.num = num

    def run(self):
        while self.data:
            print('{0} get access to lock data'.format(self.num))
            d.acquire()
            sleep(10)
            print('{0} get access to lock data and reading data'.format(self.num))
            result = data.pop()
            d.release()
            sleep(10)
            print('{0} release lock data getting access to lst'.format(self.num))
            l.acquire()
            sleep(10)
            print('{0} get access to lock lst'.format(self.num))
            lst.append(result)
            l.release()
            sleep(10)
            print('{0} release lock lst'.format(self.num))


p1 = Process(data, 1).start()
p2 = Process(data, 2).start()
p3 = Process(data, 3).start()

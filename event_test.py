from threading import Thread, Event

e1 = Event()
e2 = Event()


class Writer(Thread):
    def __init__(self, x, event1, event2):
        super().__init__()
        self.event1 = event1
        self.event2 = event2
        self.x = x

    def run(self):
        while True:
            self.event1.wait()
            open(r'/Users/Ihor/Downloads/test.txt', 'a').write(str(self.x) + '\n')
            self.event1.clear()
            self.event2.set()


w1 = Writer(1, e1, e2)
w2 = Writer(2, e2, e1)
w1.start()
w2.start()
e1.set()

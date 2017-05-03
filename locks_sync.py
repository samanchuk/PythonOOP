from threading import Thread, Lock


anchor = 1
lock = Lock()


class Writer(Thread):
    def __init__(self, x, begin, end):
        super().__init__()
        self.x = x
        self.begin = begin
        self.end = end

    def run(self):
        global anchor
        while True:
            if anchor == self.begin:
                lock.acquire()
                print(self.x)
                anchor = self.end
                lock.release()


w1 = Writer(1, 1, 2)
w2 = Writer(2, 2, 1)
w1.start()
w2.start()
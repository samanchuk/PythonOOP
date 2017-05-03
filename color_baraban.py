from threading import Thread
from time import sleep

anchor = False


class Baraban(Thread):
    def __init__(self, sectors_list):
        super().__init__()
        self.sectors_list = sectors_list
        self.last_pos = ''

    def run(self):
        while True:
            local_counter = 0
            if anchor:
                element = self.sectors_list.pop(0)
                self.sectors_list.append(element)
                self.last_pos = element
                while local_counter < 500:
                    local_counter += 1
                    sleep(0.01)


def main():
    sectors = ['white', 'black', 'red', 'green', 'blue', 'yellow']
    global anchor
    br = Baraban(sectors)
    br.start()
    while True:
        player_move = input('Your move: ')
        if player_move == 'stop':
            print('Last pos:', br.last_pos)
            anchor = False
        elif player_move == 'start':
            anchor = True


main()


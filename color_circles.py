from threading import Thread
from time import sleep
from random import randint

start_game = True


class Ball(Thread):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.here = False
        self.direction = None
        self.direction_dict = {'1': 'e', '2': 'w', '3': 's', '4': 'n'}

    def get_direction(self):
        return self.direction

    def ball_place(self):
        return self.here

    def run(self):
        global start_game
        here_counter = 0
        while start_game:
            if self.here is False:
                sleep(randint(6, 12))
                self.direction = self.direction_dict.get(str(randint(1, 4)))
                print('\n{0} ball came from {1}'.format(self.color, self.direction))
                self.here = True
            elif start_game:
                while start_game and here_counter < 500:
                    here_counter += 1
                    sleep(0.1)
                    if self.here is False:
                        here_counter = 0
                        break
                else:
                    if start_game:
                        start_game = False
                        print('Game over')


class Player:
    def __init__(self, name):
        self.name = name
        self.balls_list = [Ball('red'), Ball('green'), Ball('white'), Ball('black'), Ball('yellow')]

        for ball in self.balls_list:
            ball.start()

    def run(self):
        global start_game
        print('Game started')
        while start_game:
            try:
                strike_direction = str(input()).split()
                for ball in self.balls_list:
                    if ball.color == strike_direction[0] and ball.ball_place():
                        if ball.get_direction() != strike_direction[1] or ball.color != strike_direction[0]:
                            print('Game Over')
                            start_game = False
                        else:
                            ball.here = False
                            ball.direction = strike_direction[1]
            except IndexError:
                pass

player1 = Player('Tolik').run()

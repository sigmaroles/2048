import numpy
from game import Game
from renderer import Renderer


class Main:
    def __init__(self, size=4):
        self.game = Game(size=size)
        self.end = False
        self.renderer = Renderer(self.update, size=size)

    def update(self):
        x = numpy.random.randint(-1, 3)
        self.end = self.game.play_move(x if x != 0 else -2)
        return self.game.board

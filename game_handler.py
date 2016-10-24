import game
import numpy
from player_human import HumanPlayer
from renderer import Renderer


class GameHandler:
    def __init__(self, size=5):
        self.renderer = Renderer(self.update, size=size)
        self.state = numpy.random.RandomState()
        self.board = game.init_board(size, self.state)
        self.player = HumanPlayer(self.renderer)
        self.renderer.start()

    def update(self):
        self.player.play_move(self.board, self.state)
        return self.board

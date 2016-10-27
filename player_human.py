import numpy
import game
from typing import Type


class HumanPlayer:
    def __init__(self, renderer):
        self.side = None
        self.renderer = renderer
        self.renderer.canvas.bind("<Down>", lambda event: self.change_side(0))
        self.renderer.canvas.bind("<Right>", lambda event: self.change_side(1))
        self.renderer.canvas.bind("<Up>", lambda event: self.change_side(2))
        self.renderer.canvas.bind("<Left>", lambda event: self.change_side(3))

    def play_move(self, board: numpy.ndarray, state: Type[numpy.random.RandomState]) -> int:
        if self.side is None:
            return 2
        else:
            side = self.side
            self.side = None
            return 1 if game.play_move(board, side, state) != 0 else 2

    def change_side(self, i):
        self.side = i

import numpy
import game


class HumanPlayer:
    def __init__(self, renderer):
        self.side = None
        self.renderer = renderer
        self.renderer.canvas.bind("<Down>", lambda event: self.change_side(0))
        self.renderer.canvas.bind("<Right>", lambda event: self.change_side(1))
        self.renderer.canvas.bind("<Up>", lambda event: self.change_side(2))
        self.renderer.canvas.bind("<Left>", lambda event: self.change_side(3))

    def play_move(self, board, state):
        if self.side is None:
            return 2
        else:
            side = self.side
            self.side = None
            x = game.play_move(board, side, state)
            return 1 if x != 0 else 2

    def change_side(self, i):
        self.side = i

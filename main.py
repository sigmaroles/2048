import numpy
from game import Game
from renderer import Renderer
from neural_network import NeuralNetwork


class Main:
    def __init__(self, size=5, neural_network=NeuralNetwork()):
        self.game = Game(size=size)
        self.end = False
        self.neural_network = neural_network
        self.one = False

        # Last line
        self.renderer = Renderer(self.update, size=size)

    def update(self):
        self.end = self.neural_network.play_move(self.game)
        if not self.end and not self.one:
            print("Fail!")
            self.one = True
        return self.game.board

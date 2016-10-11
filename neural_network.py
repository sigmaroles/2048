import numpy
from game import Game


class NeuralNetwork:
    def __init__(self, neural_network=None, size=5):
        self.size = size
        if neural_network is not None:
            self.neural_network = neural_network
        else:
            self.neural_network = numpy.random.rand(size ** 2, 4)

    def play_move(self, game):
        r = numpy.tanh(numpy.reshape(numpy.log2(game.board + 1), (1, game.board.size))).dot(self.neural_network).T

        has_played = False
        count = 0
        while not has_played and count < 5:
            i = numpy.argmax(r)
            x = i % 4 - 1
            has_played = game.play_move(x if x != 0 else -2)
            r[i] = -numpy.inf
            count += 1
        return has_played

    def get_child(self, variation, randstate):
        return NeuralNetwork(
            neural_network=numpy.tanh(self.neural_network + randstate.rand(*self.neural_network.shape) * variation))

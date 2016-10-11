import matplotlib.pyplot as plt
import numpy
from neural_network import NeuralNetwork
from game import Game


class Trainer:
    def __init__(self):
        self.generations = 1
        self.randstate = numpy.random.RandomState()

    def train(self, generations, neural_network=None, population=10, size=5):
        # Initialize arrays
        scores = numpy.zeros(population, dtype=int)
        neural_networks = numpy.zeros(population, dtype=object)
        plot = numpy.zeros((generations, population), dtype=int)

        # Fill neural networks
        if neural_network is not None:
            for i in range(population):
                neural_networks[i] = neural_network.get_child(0.1, self.randstate)
        else:
            for i in range(population):
                neural_networks[i] = NeuralNetwork(size=size)

        # Loop
        while self.generations < generations:
            self.generations += 1
            # Get scores
            for i in range(population):
                scores[i] = 0
                for j in range(1):
                    game = Game(size=size)
                    while neural_networks[i].play_move(game):
                        pass
                    scores[i] += game.score
            # Sort neural networks
            neural_networks = neural_networks[scores.argsort()[::-1]]

            x = scores[scores.argsort()[::-1]]
            plot[self.generations - 1] = x
            print(x)
            print("{0:.0f}%".format(self.generations / generations * 100))

            # Create childs
            for i in range(int(population / 4), population):
                neural_networks[i] = neural_networks[i - int(population / 4)].get_child(1 / self.generations, self.randstate)

        plt.plot([k for k in range(generations)], plot, "-o")
        plt.show()

        return neural_networks[0]

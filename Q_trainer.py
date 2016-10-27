import numpy
import game


class QTrainer:
    def __init__(self, size: int = 4, epochs: int = 100):
        self.size = size
        self.random_state = numpy.random.RandomState(0)
        self.Q = numpy.zeros((size ** 2, 4))
        self.gamma = 0.8
        for i in range(epochs):
            self.train()

    def train(self):
        board = game.init_board(self.size, self.random_state)
        Q_result = board.reshape((1, self.size ** 2)).dot(self.Q)[0]
        while True:
            best_action = numpy.argmax(Q_result)
            score = 0
            count = 0
            while score == 0 and count < 4:
                score = game.play_move(board, best_action, self.random_state)
                best_action = (best_action + 1) % 4
            if score == 0:
                return
            best_action = (best_action + 3) % 4
            next_Q_result = board.reshape((1, self.size ** 2)).dot(self.Q)[0]
            next_best_action = numpy.argmax(next_Q_result)
            error = numpy.zeros(4)
            print(self.Q)
            error[best_action] = 0.5 * (score + next_Q_result[next_best_action] - Q_result[best_action]) ** 2
            for i in range(self.Q.shape[0]):
                self.Q[i] -= self.gamma * error
            Q_result = next_Q_result

    def play_move(self, board, state):
        Q_result = board.reshape((1, self.size ** 2)).dot(self.Q)
        best_action = numpy.argmax(Q_result)
        score = 0
        count = 0
        while score == 0 and count < 4:
            score = game.play_move(board, best_action, state)
            best_action = (best_action + 1) % 4
        if score == 0:
            return 0
        else:
            return 1

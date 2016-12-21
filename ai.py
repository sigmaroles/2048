import numpy
import game


class AIPlayer:
    def __init__(self, model):
        self.model = model
        self.end = False

    def play_move(self, board: numpy.ndarray, state: numpy.random.RandomState) -> int:
        if not self.end:
            qval = self.model.predict(board.reshape(1, 16), batch_size=1)
            action = numpy.argmax(qval)  # take action with highest Q-value
            print('Taking action: %s' % action)
            if game.play_move(board, action, state) == 0:
                print("Error")
                self.end = True
            else:
                return 1
        else:
            return 2

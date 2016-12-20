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
            c = 0
            while (game.play_move(board, action, state) == 0 and c < 5):
                print("Error")
                action = (action + 1) % 4
                c += 1
            if c == 5:
                print("End")
                self.end = True
            return 1
        else:
            return 2

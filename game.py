import numpy
from typing import Type


def init_board(size: int = 4, state: Type[numpy.random.RandomState] = numpy.random.RandomState()) -> numpy.ndarray:
    """
    Init board
    :param size: size of the board
    :param state: numpy random state
    :return:
    """
    board = numpy.zeros((size, size), dtype=int)
    board[state.randint(0, size), state.randint(0, size)] = 2
    return board


def play_move(board: numpy.ndarray, side: int, random_state: Type[numpy.random.RandomState]) -> int:
    """
    Play a move
    :param board: board
    :param side: side (0, 1, 2, 3)
    :param random_state: numpy random state
    :return score
    """
    score = 0
    size = board.shape[0]
    direction = side % 2  # 0 down, 1 right
    sens = (side % 2 == 0) * (side - 1) + (side % 2 == 1) * (side - 2)  # -1 left, 1 right
    for i in (range(size - 1, -1, -1) if direction == 0 and sens == -1 else range(size)):
        for j in (range(size - 1, -1, -1) if direction == 1 and sens == -1 else range(size)):
            a = (i, j)
            if board[a] != 0:
                b = (i + (direction == 0) * sens, j + (direction == 1) * sens)
                if 0 <= b[0] < size > b[1] >= 0 and (board[a] == board[b] or board[b] == 0):
                    board[b] += board[a]
                    score += board[a]
                    board[a] = 0
    if score != 0:
        x = random_state.randint(0, size ** 2)
        while board[x // size, x % size] != 0:
            x = (x + 1) % size ** 2

        board[x // size, x % size] = 2 + 2 * (random_state.rand() > 0.8)
    return score

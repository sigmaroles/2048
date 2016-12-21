import numpy


def init_board(size: int, state: numpy.random.RandomState) -> numpy.ndarray:
    """
    Init board
    :param size: size of the board
    :param state: numpy random state
    :return:
    """
    board = numpy.zeros((size, size), dtype=int)
    board[state.randint(0, size), state.randint(0, size)] = 2
    return board


def play_move(board: numpy.ndarray, side: int, state: numpy.random.RandomState) -> int:
    """
    Play a move
    :param board: board
    :param side: side (0, 1, 2, 3) (down, right, up, left)
    :param state: numpy random state
    :return score
    """
    score = 0
    size = board.shape[0]
    direction = side % 2  # 0 down, 1 right
    sens = (direction == 0) * (side - 1) + (direction == 1) * (side - 2)  # -1 down/right, 1 up/down
    for i in (range(size - 1, -1, -1) if sens == -1 else range(size)):
        for j in range(size):
            a = (i, j) if direction == 0 else (j, i)
            b = (i + sens, j) if direction == 0 else (j, i + sens)
            while 0 <= b[0] < size > b[1] >= 0 <= a[0] < size > a[1] >= 0 and (board[a] == board[b] or board[a] == 0):
                board[a] += board[b]
                score += board[b]
                board[b] = 0
                a = (a[0] - sens, a[1]) if direction == 0 else (a[0], a[1] - sens)
                b = (b[0] - sens, b[1]) if direction == 0 else (b[0], b[1] - sens)
    if score != 0:
        x = state.randint(0, size ** 2)
        while board[x // size, x % size] != 0:
            x = (x + 1) % size ** 2

        board[x // size, x % size] = 2 + 2 * (state.rand() > 0.8)
    return score


def get_reward(board: numpy.ndarray, score: int):
    reward = numpy.count_nonzero(board == 0)
    if score == 0:
        return -10
    else:
        return reward

import numpy


class Game:
    def __init__(self, size=4):
        self.size = size
        self.board = numpy.zeros((self.size, self.size), dtype=int)
        self.board[numpy.random.randint(0, self.size), numpy.random.randint(0, self.size)] = 2
        self.score = 0

    def play_move(self, side):
        """
        Play a move
        :param side: 1: right, 2: up, -1: left, -2: down
        :return: true if possible move
        """
        a = range(self.size, -1, -1) if side < 0 else range(self.size)
        has_played = False
        for i in a:
            for j in a:
                if abs(side) == 1:
                    x = i - side
                    y = j
                else:
                    x = i
                    y = j - int(side / abs(side))

                if self.size > x > -1 < y < self.size and \
                        (self.board[x, y] == self.board[i, j] != 0 or self.board[i, j] == 0):
                    has_played = True
                    self.score += self.board[x, y]
                    self.board[i, j] += self.board[x, y]
                    self.board[x, y] = 0

        if has_played:
            a = numpy.random.randint(0, self.size ** 2)
            k = 0
            while self.board[a % self.size, a // self.size] != 0 and k < self.size * 3:
                a = (a + 1) % self.size ** 2
                k += 1

            if self.board[a % self.size, a // self.size] == 0:
                self.board[a % self.size, a // self.size] = 2 if numpy.random.rand() > 0.2 else 4
            else:
                print("Game Over")
        return has_played

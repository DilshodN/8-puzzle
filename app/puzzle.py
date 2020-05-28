from copy import deepcopy


class Puzzle:
    def __init__(self, board: list):
        self.board = board
        self.len = len(board)
        if self.len == 3:
            self.goal = [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]]

    def print_matrix(self) -> str:
        output = ''
        for row in self.board:
            for elem in row:
                output += str(elem) + " "
            output += '\n'
        return output

    def get_index(self, matrix, value) -> tuple:
        for i in range(self.len):
            for j in range(self.len):
                if matrix[i][j] == value:
                    return i, j

    def manhattan(self):
        distance = 0
        for i in range(self.len):
            for j in range(self.len):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, self.len)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def list_of_possible_moves(self) -> list:
        x, y = self.get_index(self.board, 0)
        possible_moves = []
        if x > 0:
            possible_moves.append((x - 1, y))
        if x < self.len - 1:
            possible_moves.append((x + 1, y))
        if y > 0:
            possible_moves.append((x, y - 1))
        if y < self.len - 1:
            possible_moves.append((x, y + 1))
        return possible_moves

    def move(self, to: tuple) -> list:
        moving_board = deepcopy(self.board)
        x, y = self.get_index(self.board, 0)
        i, j = to
        moving_board[x][y], moving_board[i][j] = moving_board[i][j], moving_board[x][y]
        return moving_board

    def solved(self) -> bool:
        return self.board == self.goal

    def __str__(self) -> str:
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row
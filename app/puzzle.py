from copy import deepcopy


class Puzzle:
    """
    Class of puzzle game
    """
    def __init__(self, board: list):
        """
        Constructor
        """
        self.board = board
        self.len = len(board)
        if self.len == 3:
            self.goal = [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]]

    def print_matrix(self) -> str:
        """
        Prints game-board beautiful
        """
        output = ''
        for row in self.board:
            for elem in row:
                output += str(elem) + " "
            output += '\n'
        return output

    def get_index(self, matrix: list, value: int) -> tuple:
        """
        returns indexes of element of a matrix
        """
        for i in range(self.len):
            for j in range(self.len):
                if matrix[i][j] == value:
                    return i, j

    def get_zero_index(self):
        """
        returns indexes of 'zero'
        """
        for i in range(self.len):
            for j in range(self.len):
                if self.board[i][j] == 0:
                    return i, j

    def manhattan(self):
        """
        manhattan distance of the game-board
        """
        distance = 0
        for i in range(self.len):
            for j in range(self.len):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, self.len)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def list_of_possible_moves(self) -> list:
        """
        returns list of possible moves
        """
        x, y = self.get_zero_index()
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
        """
        returns moved board
        """
        moving_board = deepcopy(self.board)
        x, y = self.get_index(self.board, 0)
        i, j = to
        moving_board[x][y], moving_board[i][j] = moving_board[i][j], moving_board[x][y]
        return moving_board

    def solved(self) -> bool:
        """
        Is board solved or not?
        Yes? - true !
        No? - false !
        """
        return self.board == self.goal

    def __str__(self) -> str:
        """
        returns string variation of a board
        [[1, 2, 3],
        [4, 5, 6],    ------> '123456780'
        [7, 8, 0]]
        """
        return ''.join(map(str, self))

    def __iter__(self)->list:
        """
        returns rows from the board one-by-one
        """
        for row in self.board:
            yield from row
from copy import deepcopy
from collections import deque
from time import perf_counter


most_hard = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]  # 30 moves


class CheckPuzzle:
    def __init__(self, puzzle: list):
        self.puzzle = puzzle
        self.len = len(puzzle)
        if self.len == 3:
            self.goal = [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]]
        elif self.len == 4:
            self.goal = [[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 0]]
        if not self.is_valid():
            raise TypeError("Puzzle is not valid")
        elif not self.is_solvable():
            raise Exception("Unsolvable puzzle")

    #  создай ф-ию check

    def sum_of_numbers(self) -> int:
        return sum(self.convert_to_1d(self.goal))

    def sum_of_squares(self) -> int:
        return sum([i ** 2 for i in self.convert_to_1d(self.goal)])

    def is_valid(self) -> bool:
        sum_of_numbers = 0
        sum_of_squares = 0
        for row in range(self.len):
            for column in range(self.len):
                sum_of_numbers += self.puzzle[row][column]
                sum_of_squares += (self.puzzle[row][column]) ** 2
        return sum_of_numbers == self.sum_of_numbers() and sum_of_squares == self.sum_of_squares()

    def convert_to_1d(self, board) -> list:
        one_dimension_matrix = []
        for row in range(self.len):
            for column in range(self.len):
                one_dimension_matrix.append(board[row][column])
        return one_dimension_matrix

    def inversion(self, board) -> int:
        inversion = 0
        one_dimension_matrix = self.convert_to_1d(board)
        for index in range(len(one_dimension_matrix)):
            temp = one_dimension_matrix[index]
            if temp == 0 or temp == 1:
                continue
            for elem in one_dimension_matrix[index:]:
                if elem == 0:
                    continue
                if temp > elem:
                    inversion += 1
        return inversion

    def is_solvable(self) -> bool:
        inv_of_matrix = self.inversion(self.puzzle)
        inv_of_goal_matrix = self.inversion(self.goal)
        return (inv_of_matrix % 2 == 0 and inv_of_goal_matrix % 2 == 0) or \
               (inv_of_matrix % 2 == 1 and inv_of_goal_matrix % 2 == 1)


class Puzzle:
    def __init__(self, board: list):
        self.board = board
        self.len = len(board)
        if self.len == 3:
            self.goal = [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]]
        elif self.len == 4:
            self.goal = [[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 0]]

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


class Node:
    def __init__(self, puzzle, parent=None):
        self.puzzle = puzzle
        self.parent = parent
        if self.parent:
            self.g = parent.g + 1
        else:
            self.g = 0

    def state(self) -> str:
        return str(self)

    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    def solved(self) -> bool:
        return self.puzzle.solved()

    def pretty_print(self) -> str:
        return self.puzzle.print_matrix()

    def h(self) -> int:
        return self.puzzle.manhattan()

    def f(self) -> int:
        return self.h() + self.g

    def all_moves(self) -> list:
        return self.puzzle.list_of_possible_moves()

    def __str__(self) -> str:
        return str(self.puzzle)

    def make_a_move(self, to: tuple) -> list:
        return self.puzzle.move(to)


class GameTree:
    def __init__(self, root):
        self.root = root

    def solve(self):
        queue = deque([Node(self.root)])
        seen = set()
        seen.add(queue[0].state())
        while queue:
            queue = deque(sorted(list(queue), key=lambda node: node.f()))
            node = queue.popleft()
            if node.solved():
                return node.path()

            for move in node.all_moves():
                moved = node.make_a_move(move)
                child = Node(Puzzle(moved), node)

                if child.state() not in seen:
                    queue.append(child)
                    seen.add(child.state())
#
#
# def main():
#     a = [[5, 4, 3], [0, 7, 2], [6, 1, 8]]
#     c = Puzzle(a)
#     d = GameTree(c)
#     tic = perf_counter()
#     p = d.solve()
#     toc = perf_counter()
#     step = 0
#     for i in p:
#         print(i.pretty_print())
#         step += 1
#     print(step)
#     print(toc-tic)
#
#
# if __name__ == "__main__":
#     main()

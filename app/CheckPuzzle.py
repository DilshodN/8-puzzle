class CheckPuzzle:
    def __init__(self, puzzle: list):
        self.puzzle = puzzle
        self.len = len(puzzle)
        if self.len == 3:
            self.set = {i for i in range(9)}
            self.set.add(0)
            self.goal = [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]]

    def check(self):
        if not self.is_valid():
            raise Exception("Invalid puzzle")
        elif not self.is_solvable():
            raise Exception("Unsolvable puzzle")
        return True

    def is_valid(self) -> bool:
        for row in range(self.len):
            for col in range(self.len):
                if self.puzzle[row][col] in self.set:
                    self.set.discard(self.puzzle[row][col])
                    if len(self.set) == 0:
                        return True
        return False

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
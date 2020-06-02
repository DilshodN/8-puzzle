from puzzle import *
from heapq import *


class Node:
    """
    Constructor of Node in GameTree
    """
    def __init__(self, puzzle: Puzzle, parent: Puzzle = None):
        """
        Constructor
        """
        self.puzzle = puzzle
        self.parent = parent
        if self.parent:
            self.g = parent.g + 1
        else:
            self.g = 0

    def state(self) -> str:
        return str(self)

    def path(self):
        """
        returns generator
        """
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    def list_path(self)->list:
        """
        returns list solution from path
        """
        list_path = []
        for state in self.path:
            list_path.append(state.board)
        return list_path[1:]

    def solved(self) -> bool:
        """
        solved or not?
        returns true if 'yes'
        false if not
        """
        return self.puzzle.solved()

    def pretty_print(self) -> str:
        """
        pretty print of game-board
        """
        return self.puzzle.print_matrix()

    def h(self) -> int:
        """
        h(x) function
        """
        return self.puzzle.manhattan()

    def f(self) -> int:
        """
        f(x) = h(x) + g(x)
        """
        return self.h() + self.g

    def all_moves(self) -> list:
        """
        returns list of moves
        """
        return self.puzzle.list_of_possible_moves()

    def __str__(self) -> str:
        """
        string variation of a board
        """
        return str(self.puzzle)

    def make_a_move(self, to: tuple) -> list:
        """
        makes a move
        """
        return self.puzzle.move(to)

    def __lt__(self, other)->bool:
        """
        'less than' of the Node class
        that compares f - values the boards
        """
        return self.f() < other.f()

    def __gt__(self, other)->bool:
        """
        'greater than' of the Node class
        that compares f - values the boards
        """
        return self.f() > other.f()


class GameTree:
    """
    GAME TREE!
    """
    def __init__(self, root: Puzzle):
        """
        Constructor of a GameTree
        """
        self.root = root

    def solve(self):
        """
        [1] We create a priority queue
        [2] push to PQ tuple like (F-value of a Board, Board)
        [3] Create a quantity "SEEN" and add to the "SEEN" initial Board
        While in PQ exists something, we repeat:
            [4] get and delete from PQ value and node that has minimum f-value
            [5] Check this board, if the board is solved
                returns path of the solution if board is solved
            if not:
                 [6] Get all possible moves of our board
                 [7] we made a move
                 [8] and create a new Node
                 if out child is 'SEEN' quantity:
                    we pass
                 else:
                     we repeat [2]
                     we repeat [3]
        """
        priority_queue = []
        heappush(priority_queue, (Node(self.root).f(), Node(self.root)))
        seen = set()
        seen.add(Node(self.root).state())
        while priority_queue:
            value, node = heappop(priority_queue)
            if node.solved():
                return node.path()

            for move in node.all_moves():
                moved = node.make_a_move(move)
                child = Node(Puzzle(moved), node)

                if child.state() not in seen:
                    heappush(priority_queue, (child.f(), child))
                    seen.add(child.state())
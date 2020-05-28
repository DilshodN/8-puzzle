from puzzle import *
from heapq import *


class Node:
    def __init__(self, puzzle: Puzzle, parent: Puzzle = None):
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

    def __lt__(self, other):
        return self.f() < other.f()

    def __gt__(self, other):
        return self.f() > other.f()


class GameTree:
    def __init__(self, root: Puzzle):
        self.root = root

    def solve(self):
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
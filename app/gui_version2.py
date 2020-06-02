import tkinter as tk
from puzzle import *
from CheckPuzzle import *
from GameTree import *
from PIL import Image, ImageTk
import random
import time

IMAGES = {1: 'tile1.png', 2: 'tile2.png', 3: 'tile3.png',
          4: 'tile4.png', 5: 'tile5.png', 6: 'tile6.png',
          7: 'tile7.png', 8: 'tile8.png', 0: 'tile0.png'}


class App:
    """
    APPLICATION CLASS
    """
    def __init__(self, master, puzzle: Puzzle):
        """
        Constructor
        """
        self.master = master
        self.canvas = tk.Canvas(master, width=480, height=480)
        self.canvas.grid()
        self.puzzle = puzzle
        self.len = 3
        self.steps = 0
        self.memory = []
        self.create_events()
        self.update()
        self.shuffle(object)

    def create_events(self):
        """
        create events
        """
        self.canvas.bind_all('<KeyPress-Up>', self.slide)
        self.canvas.bind_all('<KeyPress-Down>', self.slide)
        self.canvas.bind_all('<KeyPress-Left>', self.slide)
        self.canvas.bind_all('<KeyPress-Right>', self.slide)
        self.canvas.bind_all('<space>', self.solve)
        self.canvas.bind_all('<s>', self.shuffle)
        self.canvas.bind_all('<h>', self.help)
        self.canvas.bind_all('<q>', lambda x: self.master.quit())
        self.canvas.bind_all('<k>', self.absolute_solve)

    def absolute_solve(self, event):
        """
        PRESS <K> -> solution of a board
        """
        while not self.check_state():
            self.solve(object)

    def help(self, event):
        """
        PRESS <H> -> HELP
        """
        text = 'press <SPACE> to do a "tip" move\n' \
               'press <s> to shuffle\n' \
               'press <q> to quit'
        print(text)

    def shuffle(self, event):
        """
        PRESS <S> - SHUFFLE
        """
        for _ in range(100):
            p_moves = self.puzzle.list_of_possible_moves()
            r_move = random.choice(p_moves)
            self.puzzle = Puzzle(self.puzzle.move(r_move))
        self.update()
        self.steps = 0

    def solve(self, event):
        """
        PRESS <SPACE> -> do a 'tip' move
        """
        game_tree = GameTree(self.puzzle)
        solution = game_tree.solve()
        list_solution = []
        for state in solution:
            list_solution.append(state.puzzle.board)
        to = self.tip(list_solution[1:])
        self._slide(to)

    def tip(self, next_board)->tuple:
        """
        returns tuple of a best move
        """
        if len(next_board):
            x0, y0 = Puzzle(next_board[0]).get_zero_index()
            return x0, y0

    def slide(self, event):
        """
        slide puzzle if it is possible
        """
        legal_moves = self.pieces_around()
        directions = {'up': None,
                      'down': None,
                      'left': None,
                      'right': None}
        for (way, to) in legal_moves:
            directions[way] = to
        if event.keysym == 'Down' and directions['up']:
            self._slide(directions['up'])
        if event.keysym == 'Up' and directions['down']:
            self._slide(directions['down'])
        if event.keysym == 'Right' and directions['left']:
            self._slide(directions['left'])
        if event.keysym == 'Left' and directions['right']:
            self._slide(directions['right'])

    def _slide(self, to):
        """
        sliding
        """
        self.check_state()
        try:
            new_board = self.puzzle.move(to)
            self.puzzle = Puzzle(new_board)
            self.update()
            self.steps += 1
        except:
            pass

    def pieces_around(self)->list:
        """
        returns directions and tuples of possible move
        """
        p_moves = self.puzzle.list_of_possible_moves()
        x0, y0 = self.puzzle.get_zero_index()
        possible_directions = []
        for (x, y) in p_moves:
            if y0 == y and x0 == x + 1:
                possible_directions.append(('up', (x, y)))
            if y0 == y and x0 == x - 1:
                possible_directions.append(('down', (x, y)))
            if x0 == x and y0 == y + 1:
                possible_directions.append(('left', (x, y)))
            if x0 == x and y0 == y - 1:
                possible_directions.append(('right', (x, y)))
        return possible_directions

    def check_state(self):
        """
        Is puzzle solved?
        """
        if self.puzzle.solved():
            text = 'Congrats, you achieved in %d moves' % self.steps
            print(text)
            return True

    def erase(self):
        """
        Erase before update
        """
        self.memory = []

    def convert_to_1d(self):
        """
        2d to 1d matrix
        """
        one_dimension_matrix = []
        for row in range(self.len):
            for column in range(self.len):
                one_dimension_matrix.append(self.puzzle.board[row][column])
        return one_dimension_matrix

    # noinspection PyShadowingBuiltins
    def update(self):
        """
        update of a screen game
        """
        self.erase()
        state = self.convert_to_1d()
        images = []
        for num in state:
            images.append(IMAGES[num])
        for image in images:
            opened = Image.open(image)
            image = ImageTk.PhotoImage(
                opened)
            tile = {'id': None,
                    'image': image
                    }
            self.memory.append(tile)
        idx = 0
        for x in range(3):
            for y in range(3):
                x0 = x * 160
                y0 = y * 160
                image = self.memory[idx]['image']
                id = self.canvas.create_image(y0, x0, image=image, anchor=tk.NW)
                self.memory[idx]['id'] = id
                idx += 1


def main():
    root = tk.Tk()
    root.title('8-puzzle')
    game = Puzzle([[8, 5, 2],
                   [7, 3, 1],
                   [6, 4, 0]])
    app = App(root, game)
    root.mainloop()


if __name__ == '__main__':
    main()

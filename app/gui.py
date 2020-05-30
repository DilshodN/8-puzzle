import random
import tkinter as tk
from PIL import Image, ImageTk
from math import sqrt
import puzzle as pz
from CheckPuzzle import *


# noinspection PyAttributeOutsideInit,PyShadowingBuiltins
class App(tk.Frame):
    def __init__(self, image):
        tk.Frame.__init__(self)
        self.grid()
        self.len = 3
        self.steps = 0
        self.load_image(image)
        self.create_widgets()
        self.create_board()
        self.create_events()
        self.show()

    def load_image(self, image):
        image = Image.open(image)
        image_size = min(image.size)
        self.image = image
        self.image_size = image_size
        self.piece_size = image_size / self.len

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=self.image_size, height=self.image_size)
        self.canvas.grid()

    def create_board(self):
        self.board = []
        nums = [i for i in range(1, 9)] + [0]
        i = 0
        for x in range(self.len):
            for y in range(self.len):
                x0 = x * self.piece_size
                y0 = y * self.piece_size
                x1 = x0 + self.piece_size
                y1 = y0 + self.piece_size
                crop_image = ImageTk.PhotoImage(
                    self.image.crop((x0, y0, x1, y1)))
                tile = {'id': None,
                        'image': crop_image,
                        'p_goal': (x, y),
                        'p_curr': None,
                        'visible': True,
                        'number': nums[i]
                        }
                i += 1
                self.board.append(tile)
        self.board[-1]['visible'] = False

    def show(self):
        random.shuffle(self.board)
        while not CheckPuzzle(self.get_from_show()).bool_check():
            random.shuffle(self.board)
        idx = 0
        for x in range(self.len):
            for y in range(self.len):
                self.board[idx]['p_curr'] = (x, y)
                if self.board[idx]['visible']:
                    x0 = x * self.piece_size
                    y0 = y * self.piece_size
                    image = self.board[idx]['image']
                    id = self.canvas.create_image(
                        x0, y0, image=image, anchor=tk.NW)
                    self.board[idx]['id'] = id
                idx += 1

    def get_from_show(self):
        my_board = []
        for piece in self.board:
            my_board.append(piece['number'])
        final_puzzle = []
        lenght = len(my_board)
        m = 0
        n = int(sqrt(lenght))
        for i in range(int(sqrt(lenght))):
            final_puzzle.append(my_board[m:n])
            m = n
            n += int(sqrt(lenght))
        return final_puzzle

    def create_events(self):
        self.canvas.bind_all('<KeyPress-Up>', self.slide)
        self.canvas.bind_all('<KeyPress-Down>', self.slide)
        self.canvas.bind_all('<KeyPress-Left>', self.slide)
        self.canvas.bind_all('<KeyPress-Right>', self.slide)
        # self.canvas.bind_all('k', solve())

    def slide(self, event):
        pieces = self.get_pieces_to_move()
        if event.keysym == 'Up' and pieces['down']:
            self._slide(pieces['down'], pieces['centre'],
                        (0, -self.piece_size))
        if event.keysym == 'Down' and pieces['up']:
            self._slide(pieces['up'], pieces['centre'],
                        (0, self.piece_size))
        if event.keysym == 'Left' and pieces['right']:
            self._slide(pieces['right'], pieces['centre'],
                        (-self.piece_size, 0))
        if event.keysym == 'Right' and pieces['left']:
            self._slide(pieces['left'], pieces['centre'],
                        (self.piece_size, 0))
        self.check_status()

    def _slide(self, from_, to, coord):
        self.canvas.move(from_['id'], *coord)
        to['p_curr'], from_['p_curr'] = from_['p_curr'], to['p_curr']
        self.steps += 1

    def find_empty_tile(self):
        for tile in self.board:
            if not tile['visible']:
                return tile

    def get_pieces_to_move(self):
        pieces = {'centre': None,
                  'up': None,
                  'down': None,
                  'left': None,
                  'right': None
                  }
        e_tile = self.find_empty_tile()
        pieces['centre'] = e_tile
        x0, y0 = e_tile['p_curr']
        for piece in self.board:
            x1, y1 = piece['p_curr']
            if x0 == x1 and y1 == y0 - 1:
                pieces['up'] = piece
            if x0 == x1 and y1 == y0 + 1:
                pieces['down'] = piece
            if y0 == y1 and x1 == x0 - 1:
                pieces['left'] = piece
            if y0 == y1 and x1 == x0 + 1:
                pieces['right'] = piece
        return pieces

    def check_status(self):
        for piece in self.board:
            if piece['p_curr'] != piece['p_goal']:
                return
        message = 'Вы решили за  %d ходов!' % self.steps
        print(message)


def main():
    app = App('tiles.png')
    app.master.title('8-puzzle')
    app.master.resizable(0, 0)
    app.master.mainloop()


if __name__ == '__main__':
    main()

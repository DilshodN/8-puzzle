from CheckPuzzle import *
from puzzle import *
import random
from GameTree import *


def shuffle():
    initial = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    final_puzzle = []
    random.shuffle(initial)
    m = 0
    n = 3
    for i in range(3):
        final_puzzle.append(initial[m:n])
        m = n
        n += 3
    return final_puzzle


def test_check_puzzle():
    valid = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]
    not_solvable = [[1, 2, 3],
                    [4, 5, 6],
                    [8, 7, 0]]
    not_valid = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 7, 0]]
    assert CheckPuzzle(valid).bool_check() is True
    assert CheckPuzzle(not_solvable).bool_check() is False
    assert CheckPuzzle(not_valid).bool_check() is False
    print('pass')


def test_puzzle_lib():
    example = [[8, 1, 3],
               [4, 0, 2],
               [7, 6, 5]]
    my_puzzle = Puzzle(example)
    assert my_puzzle.manhattan() == 10
    assert my_puzzle.get_index(example, 0) == (1, 1)
    assert my_puzzle.list_of_possible_moves() == [(0, 1), (2, 1), (1, 0), (1, 2)]
    assert my_puzzle.move((0, 1)) == [[8, 0, 3],
                                      [4, 1, 2],
                                      [7, 6, 5]]
    assert my_puzzle.solved() is False
    print('pass')


def test_game_tree():
    the_most_hard_puzzle_1 = [[8, 6, 7],
                              [2, 5, 4],
                              [3, 0, 1]]
    puzzle = Puzzle(the_most_hard_puzzle_1)
    assert CheckPuzzle(the_most_hard_puzzle_1).bool_check() is True
    game_tree = GameTree(puzzle)
    path = game_tree.solve()
    steps = -1
    for _ in path:
        steps += 1
    assert steps == 31
    the_most_hard_puzzle_2 = [[6, 4, 7],
                              [8, 5, 0],
                              [3, 2, 1]]
    puzzle = Puzzle(the_most_hard_puzzle_2)
    assert CheckPuzzle(the_most_hard_puzzle_2).bool_check() is True
    game_tree = GameTree(puzzle)
    path = game_tree.solve()
    steps = -1
    for _ in path:
        steps += 1
    assert steps == 31
    print('pass')


def test_random_tests():
    solvable = 0
    unsolvable = 0
    average_steps = 0
    how_many = 100
    for i in range(how_many):
        board = shuffle()
        if not CheckPuzzle(board).bool_check():
            unsolvable += 1
            print(i, 'un:', unsolvable)
            continue
        puzzle = Puzzle(board)
        game_tree = GameTree(puzzle)
        path = game_tree.solve()
        steps = -1
        for _ in path:
            steps += 1
        average_steps += steps
        solvable += 1
        print(i, 's:', solvable)
    output = 'In ' + str(how_many) + ' random boards:\n '  \
             'There is ' + str(unsolvable) + ' unsolvable:\n ' \
             + str(solvable) + ' solvable\n' \
                               'average_steps = ' + str(average_steps/solvable) + ' \n'
    print(output)


test_check_puzzle()
test_puzzle_lib()
test_game_tree()
test_random_tests()
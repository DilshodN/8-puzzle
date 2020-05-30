from math import sqrt
import puzzle
import work_with_file
from time import perf_counter
from GameTree import *
from CheckPuzzle import *
import gui
import gui_version2


# noinspection SpellCheckingInspection
def accept_from_user():
    print("Print empty space as '0'")
    first_line = input("Enter 1-st line of a puzzle:\n").split(" ")
    second_line = input("Enter 2-nd line of a puzzle:\n").split(" ")
    third_line = input("Enter 3-rd line of a puzzle:\n").split(" ")
    input_puzzle = first_line + second_line + third_line
    int_puzzle = list(map(int, input_puzzle))
    lenght = len(int_puzzle)
    final_puzzle = []
    m = 0
    n = int(sqrt(lenght))
    for i in range(int(sqrt(lenght))):
        final_puzzle.append(int_puzzle[m:n])
        m = n
        n += int(sqrt(lenght))
    return final_puzzle


def cli_to_cli():
    print("CLI->CLI")
    final_puzzle = accept_from_user()
    print("Wait...\n")
    check_puzzle = CheckPuzzle(final_puzzle)
    check_puzzle.check()
    game = Puzzle(final_puzzle)
    tree_game = GameTree(game)
    tok = perf_counter()
    solution = tree_game.solve()
    tic = perf_counter()
    print('Solution:\n')
    step = -1
    for state in solution:
        print(state.pretty_print())
        step += 1
    print('steps:', step)
    print("time:", tic - tok)


def cli_to_file():
    print("CLI->FILE")
    final_puzzle = accept_from_user()
    print("Wait...\n")
    check_puzzle = CheckPuzzle(final_puzzle)
    check_puzzle.check()
    game = Puzzle(final_puzzle)
    tree_game = GameTree(game)
    solution = tree_game.solve()
    out_file = input("Input filename: ")
    str_solution = 'SOLUTION:\n'
    step = -1
    for state in solution:
        str_solution += state.pretty_print()
        str_solution += '\n'
        step += 1
    str_solution += 'steps:' + str(step)
    work_with_file.write_puzzle(out_file, str_solution)


def file_to_cli():
    print("FILE->CLI")
    filename = input("Input filename: ")
    final_puzzle = work_with_file.read_puzzle(filename)
    print("Wait...\n")
    check_puzzle = CheckPuzzle(final_puzzle)
    check_puzzle.check()
    game = Puzzle(final_puzzle)
    tree_game = GameTree(game)
    solution = tree_game.solve()
    print('Solution:\n')
    step = -1
    for state in solution:
        print(state.pretty_print())
        step += 1
    print('steps:', step)


def file_to_file():
    print("FILE->FILE")
    filename = input("Input filename to read: ")
    final_puzzle = work_with_file.read_puzzle(filename)
    print("Wait...\n")
    check_puzzle = CheckPuzzle(final_puzzle)
    check_puzzle.check()
    game = Puzzle(final_puzzle)
    tree_game = GameTree(game)
    solution = tree_game.solve()
    out_file = input("Input filename to write: ")
    str_solution = 'SOLUTION:\n'
    step = -1
    for state in solution:
        str_solution += state.pretty_print()
        str_solution += '\n'
        step += 1
    str_solution += 'steps:' + str(step)
    work_with_file.write_puzzle(out_file, str_solution)
    print('\nSUCCESS\n')


def GUI():
    gui.main()


def GUI_with_tips():
    gui_version2.main()

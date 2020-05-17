from math import sqrt
import puzzle
import work_with_file


def accept_from_user():
    print("Print empty space as '0'")
    first_line = input("Enter 1-st line of a puzzle:\n").split(" ")  # ['5', '8', '0']
    second_line = input("Enter 2-nd line of a puzzle:\n").split(" ")  # ['7', '6', '1']
    third_line = input("Enter 3-rd line of a puzzle:\n").split(" ")  # ['3', '2', '4']
    input_puzzle = first_line + second_line + third_line
    int_puzzle = list(map(int, input_puzzle))
    lenght = (len(int_puzzle))
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
    check_puzzle = puzzle.CheckPuzzle(final_puzzle)
    game = puzzle.Puzzle(final_puzzle)
    tree_game = puzzle.GameTree(game)
    solution = tree_game.solve()
    print('Solution:\n')
    step = 0
    for state in solution:
        print(state.pretty_print())
        step += 1
    print('steps:', step)


def cli_to_file():
    print("CLI->FILE")
    final_puzzle = accept_from_user()
    print("Wait...\n")
    check_puzzle = puzzle.CheckPuzzle(final_puzzle)
    game = puzzle.Puzzle(final_puzzle)
    tree_game = puzzle.GameTree(game)
    solution = tree_game.solve()
    out_file = input("Input filename: ")
    str_solution = 'SOLUTION:\n'
    step = 0
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
    check_puzzle = puzzle.CheckPuzzle(final_puzzle)
    game = puzzle.Puzzle(final_puzzle)
    tree_game = puzzle.GameTree(game)
    solution = tree_game.solve()
    print('Solution:\n')
    step = 0
    for state in solution:
        print(state.pretty_print())
        step += 1
    print('steps:', step)



def file_to_file():
    print("FILE->FILE")
    filename = input("Input filename to read: ")
    final_puzzle = work_with_file.read_puzzle(filename)
    print("Wait...\n")
    check_puzzle = puzzle.CheckPuzzle(final_puzzle)
    game = puzzle.Puzzle(final_puzzle)
    tree_game = puzzle.GameTree(game)
    solution = tree_game.solve()
    out_file = input("Input filename to write: ")
    str_solution = 'SOLUTION:\n'
    step = 0
    for state in solution:
        str_solution += state.pretty_print()
        str_solution += '\n'
        step += 1
    str_solution += 'steps:' + str(step)
    work_with_file.write_puzzle(out_file, str_solution)
    print('\nSUCCESS\n')
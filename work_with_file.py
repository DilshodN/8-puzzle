from math import sqrt


def read_puzzle(filename: str) -> list:
    arr_puz = []
    with open(filename, 'r') as file:
        try:
            puzzle = file.read()
            for char in puzzle:
                if char == '\n' or char == ' ':
                    continue
                arr_puz.append(char)
            lenght = len(arr_puz)
            arr_puz = list(map(int, arr_puz))
            canon = []
            m = 0
            n = int(sqrt(lenght))
            for i in range(int(sqrt(lenght))):
                canon.append(arr_puz[m:n])
                m = n
                n += int(sqrt(lenght))
            return canon

        except:
            raise TypeError("\nProblems with file!\n"
                            "Your puzzle should be 3x3\n"
                            "Empty space must be '0'\n")


def write_puzzle(to_file: str, solution: str):
    with open(to_file, "w") as file:
        file.write(solution)

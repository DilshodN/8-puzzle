import work_with_user


def main():
    flag = True
    print("\nHello!\n"
          'This is 8-puzzle python script')
    while flag:
        print('This script has 4-modes to work\n'
              '[1] -> from CLI to CLI\n'
              '[2] -> from CLI to FILE\n'
              '[3] -> from FILE to CLI\n'
              '[4] -> from FILE to FILE\n'
              '[5] -> play GUI version')
        try:
            mode = int(input('Input mode: '))
        except:
            raise TypeError("Error Input")
        if mode > 5 or mode < 1:
            raise Exception("Mode should be 1, 2, 3, 4 or 5")
        if mode == 1:
            work_with_user.cli_to_cli()
        if mode == 2:
            work_with_user.cli_to_file()
        if mode == 3:
            work_with_user.file_to_cli()
        if mode == 4:
            work_with_user.file_to_file()
        if mode == 5:
            work_with_user.GUI()

        again = input("\nwant to continue ?\n"
                      "y/n: ")
        if again == 'y':
            flag = True
        if again == 'n':
            flag = False


if __name__ == "__main__":
    main()

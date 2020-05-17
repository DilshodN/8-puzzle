import puzzle
import work_with_file
import work_with_user


def main():
    flag = True
    print("\nHello!\n"
          'This is old_8-puzzle python script')
    while flag:
        print('This script has 4-modes to work\n'
              '1-from cli to cli\n'
              '2-from cli to file\n'
              '3-from file to cli\n'
              '4-from file to file')
        try:
            mode = int(input('Input mode: '))
        except:
            raise TypeError("Error Input")
        if mode > 4 or mode < 1:
            raise Exception("Mode should be 1, 2, 3 or 4")
        try:
            if mode == 1:
                work_with_user.cli_to_cli()
            if mode == 2:
                work_with_user.cli_to_file()
            if mode == 3:
                work_with_user.file_to_cli()
            if mode == 4:
                work_with_user.file_to_file()
        except:
            raise TypeError("Input Error")

        again = input("\nwant to continue ?"
                      "y/n\n")
        if again == 'y':
            flag = True
        if again == 'n':
            flag = False


if __name__ == "__main__":
    main()

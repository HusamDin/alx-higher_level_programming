#!/usr/bin/python3

if __name__ == '__main__':
    """Prints command line arguments"""
    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")
    if len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    if len(argv) > 2:
        for i in range(1, len(argv)):
            if i == 1:
                print("{} arguments:".format(len(argv) - 1))
            print("{}: {}".format(i, argv[i]))

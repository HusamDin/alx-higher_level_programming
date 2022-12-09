#!/usr/bin/python3

if __name__ == '__main__':
    """Prints command line arguments"""
    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")

    for i in range(1, len(argv)):
        if len(argv) >= 1:
            if i == 1:
                if len(argv) == 2:
                    print("{} argumnent:".format(len(argv) - 1))
                else:
                    print("{} argumnets:".format(len(argv) - 1))
            print("{}: {}".format(i, argv[i]))

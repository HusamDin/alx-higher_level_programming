#!/usr/bin/python3

if __name__ == '__main__':
    """"Print the result of the addition of all arguments"""
    from sys import argv

    result = 0

    if len(argv) == 1:
        print(result)

    if len(argv) > 1:
        for i in range(1, len(argv)):
            result += int(argv[i])

        print(result)

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("{} {}{}".format(argc, ('argument' if argc == 1 else 'arguments'), ('.' if argc == 0 else ':')))

    for index in range(1, argc + 1):
        print("{}: {}".format(index, sys.argv[index]))

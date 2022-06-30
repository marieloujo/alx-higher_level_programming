#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    sum = 0

    for index in range(1, argc + 1):
        sum += int(sys.argv[index])

    print(sum)

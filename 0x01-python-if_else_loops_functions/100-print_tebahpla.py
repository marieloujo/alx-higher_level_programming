#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    char = chr(letter)

    if (letter % 2 != 0):
        char = chr(letter - 32)

    print("{}".format(char), end='')

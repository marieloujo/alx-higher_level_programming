#!/usr/bin/python3
import random

n = random.randint(-10000, 10000)
lastDigit = int(str(n)[-1])

if (lastDigit == 0):
    print("Last digit of {} is {} and is 0".format(n, lastDigit))

elif (lastDigit < 6):
    print("Last digit of {} is".format(n), end=" ")
    print("{} and is less than 6 and not 0".format(lastDigit))

if (lastDigit > 5):
    print("Last digit of {} is {} and is greater than 5".format(n, lastDigit))

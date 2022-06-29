#!/usr/bin/python3
import random

n = random.randint(-10000, 10000)

if n < 0:
    lastDigit = n % -10
else:
    lastDigit = n % 10

print('Last digit of', n, 'is', lastDigit, end=' ')

if lastDigit > 5:
    print('and is greater than 5')

elif lastDigit == 0:
    print('and is 0')

else:
    print('and is less than 6 and not 0')

#!/usr/bin/python3
tour = 1

for i in range(10):
    for j in range(tour, 10):
        if i == 8 and j == 9:
            print('{}{}'.format(i, j))
        else:
            print('{}{}'.format(i, j), end=', ')

    tour = tour + 1

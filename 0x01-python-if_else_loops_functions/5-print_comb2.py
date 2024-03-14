#!/usr/bin/python3
for digit in range(0, 100):
    if digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(("0{},".format(digit)), end=" ")
    else:
        print("{}".format(digit), end=", " if digit != 99 else "\n")

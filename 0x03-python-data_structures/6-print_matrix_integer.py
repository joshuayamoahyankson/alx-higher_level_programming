#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, each_element in enumerate(row):
            print("{:d}".format(each_element), end="")
            if index != len(row) - 1:
                print(" ", end="")
        print()

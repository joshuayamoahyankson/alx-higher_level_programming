#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for each_element in row:
            print("{:d}".format(each_element), end=" ")
        print()

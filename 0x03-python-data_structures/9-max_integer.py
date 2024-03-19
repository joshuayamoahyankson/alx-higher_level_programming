#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    cur_largest = my_list[0]
    for value in my_list:
        if my_list[value] > cur_largest:
            cur_largest = my_list[value]
        return cur_largest

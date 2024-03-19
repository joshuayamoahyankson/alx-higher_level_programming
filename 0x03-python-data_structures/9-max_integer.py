#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        cur_largest = my_list[0]
        for value in range(len(my_list)):
            if my_list[value] > cur_largest:
                cur_largest = my_list[value]
        return cur_largest

#!/usr/bin/python
def uniq_add(my_list=[]):
    new_set = set()
    result = 0
    for i in my_list:
        if (i not in new_set):
            new_set.add(i)
    for x in new_set:
        result += x
    return result

#!/usr/bin/python
def uniq_add(my_list=[]):
    new_set = set()
    for i in my_list:
        if (i not in new_set):
            new_set.add(i)
    return sum(new_set)

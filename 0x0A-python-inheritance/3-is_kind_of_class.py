#!/usr/bin/python3
"""A module that checks if an object is an instance
of a class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """Returns true or false depending on whether the object
    is an instance of or....false"""
    return isinstance(obj, a_class)

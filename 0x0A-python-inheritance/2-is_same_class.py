#!/usr/bin/python3
"""This module checks if an
object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Returns true or false depending on
    whether the object is an instance of a
    specified class or not"""
    return (type(obj) == a_class)

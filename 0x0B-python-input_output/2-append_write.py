#!/usr/bin/python3
"""This module defines a text file for appending"""


def append_write(filename="", text=""):
    """Using the with keyword and the 'a' value
    for appending to a file, thus code appends and returns
    the character count"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)

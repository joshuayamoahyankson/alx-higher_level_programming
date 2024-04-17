#!/usr/bin/python3
"""This module defines a text file for reading"""


def read_file(filename=""):
    """Using the with keyword, it opens in read-mode
    and prints the contents of the text file"""
    with open(filename, encoding="utf-8") as text_file:
        read_text = text_file.read()
        print(read_text)
    return read_text

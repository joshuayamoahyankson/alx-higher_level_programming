#!/usr/bin/python3
"""This module defines a text file for writing"""


def write_file(filename="", text=""):
    """Using the with keyword, this function writes
    some contents to a file and prints the number
    of characters"""
    with open(filename, mode="w", encoding="utf-8") as file:
        write_text_count = file.write(text)
    return write_text_count

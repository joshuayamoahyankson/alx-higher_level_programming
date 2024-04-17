#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, mode="rt", encoding="utf-8") as text_file:
        read_text = text_file.read()
        print(read_text)
    return read_text

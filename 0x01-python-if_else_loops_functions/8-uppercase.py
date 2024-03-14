#!/usr/bin/python3
def uppercase(str):
    upper_case = ""
    for letter in str:
        if 'a' <= letter <= 'z':
            upper_case += ("{:c}".format(ord(letter) - 32))
        else:
            upper_case += letter
    print("{}".format(upper_case), end="")
    print()

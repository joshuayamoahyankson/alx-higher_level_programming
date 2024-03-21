#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    result = 0
    for i in (sys.argv[1:]):
        if (num_args == 0):
            print(f"{num_args}")
        else:
            result += int(i)
    print(f"{result}")

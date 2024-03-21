#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1

    if length == 0:
        print(f"{length} arguments.")
    else:
        print(f"{length} {'argument' if length == 1 else 'arguments'}:")
    for index, arguments in enumerate(sys.argv[1:], start=1):
        print(f"{index}: {arguments}")

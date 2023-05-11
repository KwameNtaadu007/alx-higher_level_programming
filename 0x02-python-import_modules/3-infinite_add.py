#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    """Program prints the sum of all command line arguments."""
    import sys

    total = 0
    for j in range(len(sys.argv) - 1):
        total += int(sys.argv[j + 1])
    print("{}".format(total))

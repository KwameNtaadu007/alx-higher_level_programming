#!/usr/bin/python3

"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

from sys import argv


def nqueens(n):
    """Recursive backtracking function to find the solution"""
    def already_exists(y, a):
        """Check that a queen does not already exist in that y value"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y, a):
        """Determines whether or not to reject the solution"""
        if already_exists(y, a):
            return False
        i = 0
        while i < x:
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x, a):
        """Clears the answers from the point of failure on"""
        for i in range(x, n):
            a[i][1] = None

    def solve(x, a):
        """Helper function to solve the n-queens problem"""
        for y in range(n):
            clear_a(x, a)
            if reject(x, y, a):
                a[x][1] = y
                if x == n - 1:  # Accepts the solution
                    print(a)
                else:
                    solve(x + 1, a)  # Moves on to next x value to continue

    if n < 4:
        print("N must be at least 4")
        return

    a = [[i, None] for i in range(n)]  # Initialize the answer list
    solve(0, a)  # Start the recursive process at x = 0


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    nqueens(n)

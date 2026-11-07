#!/usr/bin/python3
"""Prints every solution to the N queens puzzle."""
import sys


def solve(n, row, solution):
    """Places a queen in each row by backtracking and prints full boards."""
    if row == n:
        print(solution)
        return
    for col in range(n):
        if all(c != col and abs(c - col) != row - r for r, c in solution):
            solution.append([row, col])
            solve(n, row + 1, solution)
            solution.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, 0, [])

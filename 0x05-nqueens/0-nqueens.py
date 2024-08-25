#!/usr/bin/python3
"""module to solve the N queens problem"""
import sys


def get_solution(input):
    """get and print all the possible solutions for placing non-attacking
    queens on an n*n chessboard"""
    if len(input) < 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(input[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    solve_nqueens(solutions, [], n, 0)
    for solution in solutions:
        print(solution)


def solve_nqueens(solutions, solution, n, index):
    """solve n queens using backtracking"""
    if len(solution) == n:
        solutions.append(solution)
        return
    for col in range(n):
        if is_valid(index, col, solution):
            test_solution = solution + [[index, col]]
            solve_nqueens(solutions, test_solution, n, index + 1)
    return None


def is_valid(row, col, solution):
    """check if a position is valid"""
    for r, c in solution:
        if col == c or abs(row - r) == abs(col - c):
            return False
    return True


if __name__ == "__main__":
    get_solution(sys.argv)
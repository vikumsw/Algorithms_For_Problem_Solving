"""
Challenge #720
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
"""


def solve_sudoku(matrix, row, col):
    if row == len(matrix) - 1 and col == len(matrix[0]):
        return True

    if col == len(matrix[0]):
        row += 1
        col = 0

    if matrix[row][col] != 0:
        return solve_sudoku(matrix, row, col + 1)

    for i in range(1, 10):
        if is_safe(matrix, row, col, i):
            matrix[row][col] = i

            if solve_sudoku(matrix, row, col + 1):
                return True

        matrix[row][col] = 0

    return False


def is_safe(matrix, x, y, i):
    return check_box(matrix, x, y, i) and check_row(matrix, x, i) and check_column(matrix, y, i)


def check_row(matrix, x, i):
    for k in range(len(matrix[x])):
        if matrix[x][k] == i:
            return False
    return True


def check_column(matrix, y, i):
    for k in range(len(matrix)):
        if matrix[k][y] == i:
            return False
    return True


def check_box(matrix, x, y, i):
    if x < 3:
        org_x = 0
    elif x < 6:
        org_x = 3
    else:
        org_x = 6

    if y < 3:
        org_y = 0
    elif y < 6:
        org_y = 3
    else:
        org_y = 6

    for a in range(org_x, org_x + 3):
        for b in range(org_y, org_y + 3):
            if matrix[a][b] == i:
                return False
    return True


def print_matrix(matrix):
    for x in range(len(matrix)):
        print("[", end='')
        for y in range(len(matrix[x])):
            print(matrix[x][y], ",", end='')
        print("],")


mat = [[0, 0, 0, 0, 9, 0, 6, 0, 5],
        [0, 8, 0, 1, 0, 6, 0, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 1, 0],
        [6, 0, 0, 0, 0, 5, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 6, 7, 8, 3, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 3, 0, 4, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 4, 0, 0]]

solve_sudoku(mat, 0, 0)
print_matrix(mat)

# n_queens.py
# Solving the N-Queens problem as a CSP
# Robert Chang
# 9/13/23

import numpy as np

# construct a 4x4 matrix of 0's
n = 4
board = np.zeros((4,4), dtype = int)

# function for printing the solution matrix
def solution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = ' ')
        print()
    print("\n")

# function for checking if a space is safe or not
def checker(board, row, column):
    # check the row
    for i in range(column):
        if board[row][i] == 1:
            return False

    # check the upward diagonal
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    # check the downward diagonal
    for i, j in zip(range(row, n, 1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
        
    # if a spot is safe, return True
    return True

# function for placing the queens
def queen_placer(board, column):
    # if all the queens are on the board, return True
    if column >= n:
        return True

    # check all the rows in a column and place a queen if empty, where 1 denotes a space with a queen
    # and 0 denotes an empty space
    for i in range(n):
        if checker(board, i, column) == True:
            board[i][column] = 1
            if queen_placer(board, column + 1) == True:
                return True
            # backtracking
            # if the queen placement doesn't yield a solution, remove the queen
            else:
                board[i][column] = 0
                
    # backtracking
    # if the queen cannot be placed, return False
    return False

queen_placer(board, 0)
solution(board)

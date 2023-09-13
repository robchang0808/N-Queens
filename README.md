# N-Queens
Python program which solves the N-Queens problem as a constraint satisfaction problem. The N-Queens problem involves placing the greatest number of queens on a chessboard, where no queen is attacking another queen.

# Logistics
The program is coded in Python and requires the numpy import to construct the chessboard. The chessboard is represented by a matrix of 0's and 1's, where each 0 represents an empty space and each 1 represents a queen. The program yields the final board as a matrix as the output. 

# Process
The N-Queens problem is a classic CSP. In this program, the number of queens (n) and the size of the board can be modified accordingly. Naturally, the number of queens should correspond with the dimensions of the chessboard: a 4x4 board would mean n=4. Any more queens and a column/row would have two queens, any less and the board would not be optimal. 

The constraint of this CSP is the rule that no queen can attack another queen. This constraint is met through the checker function. For a space in a given column, the checker function passes through the row and diagonals that the specified space resides in, ensuring that no 1's exist in the spaces it passes through. If there isn't, the specified space is changed from 0 to 1. If there is, the space remains a 0 and the next corresponding space in the column is checked.

In the case where a queen cannot be placed in any of the spaces in a column, the backtracking is performed and the queen in the previous column is removed. Then starting from the subsequent space in the previous column, the checker process is repeated to find a new space for the queen in the previous column. Depending on the board, this backtracking process may be performed once, twice, or many times until the optimal board is achieved. 

Once the optimal board is reached, the program prints the board in 0's and 1's. The code provided visualizes a 4x4 board with 4 queens placed on it. The file "4_queens_result.png" shows the final board. 

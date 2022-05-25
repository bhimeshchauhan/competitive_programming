"""

maximal-square

"""


"""
The idea is to use input matrix itself as the resultant matrix. To do this we'll have to handle few edge cases:

if matrix contains all 0's.
if matrix has one row or one column.
Thinking process:

We use is_row_one and is_col_one to store if our first row & column has any 1 or not.
We then check if matrix has one row (e.g. [["1", "0"]], then it that case result will depend on if there is any 1 in the matrix (since each 1 creates a square of size 1*1=1). This is stored in is_row_one.
Similarly for matrix with one column (e.g. [["1"],["0"]]).
max_side stores maximum length of square.
If none of the is_col_one or is_row_one are 1, then we can for time being initialize max_side with 0. This is done so that if in case the whole matrix if of 0's (e.g. [["0", "0"], ["0", "0"]]). max_side will be updated later on with val >= 1 if there is a 1 in matrix.
Square can be made from posiltion (i, j) with value 1. That's why the check if matrix[i][j] == '1':.
Suppose if we are at (i=2, j=2), then to make a square we need to have 1 in top (i-1, j), left(i, j-1) and top-left diagonal (i-1, j-1). Code: matrix[i][j] = min(int(matrix[i-1][j-1]), int(matrix[i-1][j]), int(matrix[i][j-1])) + 1
Above code makes sure that if any of the matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1] is 0, matrix[i][j] will be 1. If all of them are 1, then matrix[i][j] will be atleast 1.
Max square size will be max_side*max_side

"""




from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        is_row_one, is_col_one = 0, 0

        for col_val in matrix[0]:
            if col_val == '1':
                is_row_one = 1
                break

        for row in matrix:
            if row[0] == '1':
                is_col_one = 1
                break

        if len(matrix) == 1:
            return is_row_one

        if len(matrix[0]) == 1:
            return is_col_one

        max_side = 0
        if is_col_one or is_row_one:
            max_side = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i-1][j-1]),
                                       int(matrix[i-1][j]), int(matrix[i][j-1])) + 1
                    max_side = max(max_side, matrix[i][j])
        return max_side*max_side

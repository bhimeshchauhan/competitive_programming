"""


"""


"""

- Let (x, y) be the bottom-right corner of multiple squares of different sizes.
- Let matrix[x][y] be the number of squares whose the bottom-right corner is (x, y). matrix[x][y] is also the width of the biggest square whose the bottom-right corner be (x, y).

Now comes the DP part:

- We skip (x, y) whose original matrix[x][y] value is 0 because they cannot be the bottom-right corner of any squares.
Consider matrix[x][y] as the width of the biggest square whose the bottom-right corner be (x, y).
matrix[x][y] = n if and only if matrix[x - 1][y] = matrix[x][y - 1] = matrix[x - 1][y - 1] = n - 1.
- What will happen if matrix[x - 1][y], matrix[x][y - 1] and matrix[x - 1][y - 1] does not share the same value? Let's look at the following illustration of a matrix in the mid of computation:
| 1 | 1 | 1 | 0 |
| 1 | 2 | 2 | 0 |
| 1 | 2 | 3 | 1 |
| 0 | 0 | 1 | ? |

where matrix[x - 1][y] = matrix[x][y - 1] = 1 and matrix[x - 1][y - 1] = 3. It turns out matrix[x][y] = 2.

Or, to be more generic:

matrix[x][y] = min(matrix[x - 1][y], matrix[x][y - 1], matrix[x - 1][y - 1]) + 1

"""


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        count = sum(matrix[0])
        for i in range(1, len(matrix)):
            count += matrix[i][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i - 1][j], matrix[i]
                                   [j - 1], matrix[i - 1][j - 1]) + 1
                count += matrix[i][j]

        return count

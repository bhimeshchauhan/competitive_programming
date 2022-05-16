"""

Unique Paths

https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100

"""


from functools import cache
from itertools import product
from math import factorial

"""
Time Complexity : O(m*n), the answer to each of cell is calculated only once and memoized. There are m*n cells in total and thus this process takes O(m*n) time.
Space Complexity : O(m*n), required to maintain dp.
"""


class Solution:
    def uniquePaths(self, m, n):
        @cache
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)


"""
Time Complexity : O(m*n), we are computing dp values for each of the m*n cells from the previous cells value. Thus, the total number of iterations performed is requires a time of O(m*n).
Space Complexity : O(m*n), required to maintain the dp matrix
"""


class Solution:
    def uniquePaths(self, m, n):
        dp = [[1]*n for i in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


"""
Time Complexity : O(m*n), for computing dp values for each of the m*n cells.
Space Complexity : O(n), required to maintain dp. We are only keeping two rows of length n giving space complexity of O(n).
There's a small change that can allow us to optimize the space complexity down to O(min(m, n)).
"""


class Solution:
    def uniquePaths(self, m, n):
        dp = [1]*n
        for _, j in product(range(1, m), range(1, n)):
            dp[j] += dp[j-1]
        return dp[-1]


"""
We start at (0, 0) cell and move to (m-1, n-1) cell.
We need to make m-1 down-moves and n-1 right-moves to reach the destination cell.
Thus, we need to perform a total number of m+n-2 moves.
At each cell along the path, we can choose either the right-move or down-move and we need to find the number of unique combinations of these choices (which eventually leads to unique paths).
This is nothing but calculating the number of different ways to choose m-1 down-moves and n-1 right-moves from a total of m+n-2 moves. Mathematically, this can be represented as 
"""

"""
Time Complexity : O(min(m,n)) for C++, and O(m+n) for Python. We could do it in O(min(m,n)) for python as well using technique used in C++.
Space Complexity : O(1)
"""


class Solution:
    def uniquePaths(self, m, n):
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)

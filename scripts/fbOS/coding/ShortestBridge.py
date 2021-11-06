"""

Shortest Bridge

In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:

Input: grid = [
    [0,1],
    [1,0]
]
Output: 1

Example 2:

Input: grid = [
    [0,1,0],
    [0,0,0],
    [0,0,1]
]
Output: 2

Example 3:

Input: grid = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]
Output: 1

Constraints:

2 <= grid.length == grid[0].length <= 100
grid[i][j] == 0 or grid[i][j] == 1

"""

from collections import deque

"""
- Paint the first encountered island with the color '2'
- Start expanding this island by painting connected 'empty' cells
- For every successive round, increase value of 'color' by 1 (This helps us keep track of the number of steps required)
- End when we bump into an island i.e. when we encounter a cell with value '1' (original island which wasn't colored '2')
- The answer is the difference of the current color value and '2' (the starting color)

"""


class Solution:
    # Assigning '2' to one of the islands
    def paint(self, A, i, j):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]) or A[i][j] == 0 or A[i][j] == 2:
            return
        A[i][j] = 2
        for nb in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self.paint(A, i + nb[0], j + nb[1])

    # expanding from the perimeter of the island & incrementing color with every next outward move
    def expand(self, A, i, j, color):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]):
            return False
        if A[i][j] == 0:
            A[i][j] = color + 1
        return A[i][j] == 1

    def shortestBridge(self, A):
        if not A:
            return 0
        m, n, flag = len(A), len(A[0]), False

        # Finding and coloring the first encountered island
        for i in range(m):
            if flag:
                break
            for j in range(n):
                if A[i][j] == 1:
                    self.paint(A, i, j)
                    flag = True
                    break

        # Growing outward and tracking number of steps taken to bump into other island
        for color in range(2, 2+m+n+1):
            for i in range(m):
                for j in range(n):
                    if A[i][j] == color and (self.expand(A, i-1, j, color) or self.expand(A, i, j+1, color) or
                                             self.expand(A, i+1, j, color) or self.expand(A, i, j-1, color)):
                        return color-2


if __name__ == "__main__":
    grid = [[0, 1], [1, 0]]
    print(Solution().shortestBridge(grid))

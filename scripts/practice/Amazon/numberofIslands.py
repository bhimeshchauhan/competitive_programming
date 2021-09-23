"""

Number of Islands

Given an m x n 2D binary grid grid which represents a map of 
'1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

# BFS

"""

Complexity Analysis

Time complexity : O(M×N) where M is the number of rows 
    and N is the number of columns.

Space complexity : O(min(M,N)) because in worst case 
where the grid is filled with lands, the size of 
queue can grow up to min(M,N).

"""

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])
        count = 0
        dirxn = [[0,1], [1,0], [0,-1], [-1,0]]
        for row in range(R):
            for col in range(C):
                q = deque()
                if grid[row][col] == '1':
                    q.append([row, col])
                    grid[row][col] = '0'
                    count += 1
                while q:
                    idx, jdy = q.popleft()
                    for dx, dy in dirxn:
                        x = dx + idx
                        y = dy + jdy
                        if 0 <= x < R and 0 <= y < C and grid[x][y] == '1':
                            q.append([x, y])
                            grid[x][y] = '0'
        return count

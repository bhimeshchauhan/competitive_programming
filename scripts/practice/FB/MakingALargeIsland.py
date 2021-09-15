"""

Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

"""

from collections import defaultdict

class Solution:
    def largestIsland(self, grid):
        visited, number = set(), 2
        #Run DFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]==1:
                    visited.add((i,j))
                    self.dfs(grid, visited, i, j, number)
                    number+=1
        #Count Group Elements in set
        zeroLoc, groupElemCounter = set(), defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0: zeroLoc.add((i,j))
                else: groupElemCounter[grid[i][j]]+=1
        #Calculate result
        if len(zeroLoc)==0: return len(grid)*len(grid[0])
        largeIsland = float("-inf")
        for (i,j) in zeroLoc:
            direction, nearIslands = [(0,1), (0,-1), (1,0), (-1,0)], set()
            for (dx,dy) in direction:
                x, y = i+dx, j+dy
                if 0<=x<len(grid) and 0<=y<len(grid[0]): nearIslands.add(grid[x][y])
            #Now Calculate total after converting that 0 to 1
            total = 1
            for i in nearIslands:
                total+=groupElemCounter[i]
            largeIsland = max(largeIsland, total)
        return largeIsland

    def dfs(self, grid, visited, x, y, groupNumber = 2):
        grid[x][y] = groupNumber
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        for (dx,dy) in direction:
            ax, ay = x+dx, y+dy
            if 0<=ax<len(grid) and 0<=ay<len(grid[0]) and (ax,ay) not in visited  and grid[ax][ay]==1:
                visited.add((ax,ay))
                self.dfs(grid, visited, ax, ay, groupNumber)
                

if __name__ == "__main__":
    mat = [[1, 0], [0, 1]]
    print(Solution().largestIsland(mat))

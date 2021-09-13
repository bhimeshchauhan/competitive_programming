"""

Shortest Bridge

In a given 2D binary array grid, there are two islands.  
(An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

2 <= grid.length == grid[0].length <= 100
grid[i][j] == 0 or grid[i][j] == 1

"""
from collections import deque


class Solution:
    def findFirst(self, grid, row, col):
        dirxn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0 or grid[row][col] == 2:
            return
        grid[row][col] = 2
        for dx, dy in dirxn:
            self.findFirst(grid, row+dx, col+dy)

    def isEdge(self, grid, row, col):
        dirxn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in dirxn:
            newR = row + dx
            newC = col + dy
            if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]):
                print(newR, newC)
                if grid[newR][newC] == 0:
                    return True
        return False

    def shortestBridge(self, grid):
        R = len(grid)
        C = len(grid[0])

        q = deque()
        islandEdge = 0
        dirxn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # find first island
        flag = False
        for row in range(R):
            if flag:
                break
            for col in range(C):
                if grid[row][col] == 1:
                    self.findFirst(grid, row, col)
                    flag = True
                    break
        print(grid)
        flag = False
        for row in range(R):
            if flag:
                break
            for col in range(C):
                if grid[row][col] == 2 and self.isEdge(grid, row, col):
                    q.append((row, col))

        # print(grid, q)
        shortestBridge = float('inf')
        while q:
            row, col = q.popleft()
            # print('looking at ', row, col, grid)
            newVal = grid[row][col] + 1
            # grid[row][col] = newVal
            for dx, dy in dirxn:
                newR = row + dx
                newC = col + dy
                if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]):
                    if grid[newR][newC] == 0:
                        grid[newR][newC] = newVal
                        q.append((newR, newC))
                    elif grid[newR][newC] == 1:
                        print(row, col, grid[row][col])
                        shortestBridge = min(shortestBridge, grid[row][col]-2)
        # print(grid, shortestBridge)
        return shortestBridge


if __name__ == "__main__":
    grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    print(Solution().shortestBridge(grid))

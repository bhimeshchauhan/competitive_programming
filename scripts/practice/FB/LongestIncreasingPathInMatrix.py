"""

Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed). 

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        longest_path = 0
        rows = len(matrix)
        cols = len(matrix[0])
        cache = [[None] * cols for _ in range(rows)]
        
        def dfs(x: int, y: int) -> int:
            if cache[x][y]:
                return cache[x][y]
            longest_path = 0
            for i, j in [(0,1),(0,-1),(1,0),(-1,0)]:
                newX, newY = x+i, y+j
                if newX >= 0 and newX < rows and newY >= 0 and newY < cols and matrix[newX][newY] > matrix[x][y]:
                    longest_path = max(longest_path, dfs(newX, newY))
            cache[x][y] = longest_path + 1
            return cache[x][y]
        
        for x in range(rows):
            for y in range(cols):
                longest_path = max(longest_path, dfs(x, y))
        
        return longest_path
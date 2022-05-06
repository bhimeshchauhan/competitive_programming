"""

01 Matrix

https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

"""


from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        What the hell is a level?
        A level will be the 'depth' of each cell which cooresponds to it's distance
        to the nearest 0.
        Looking at EX. 2,
        the levels are (level depth -> coordinates in mat)...
        0 -> (0,0), (0,1), (0,2)
        1 -> (1,0), (1,2)
        2 -> (2,1)
        """
        # Defining the bounds of the matrix
        rows, cols = len(mat), len(mat[0])
        # Making the queue
        queue = []
        # Creating the seen set
        seen = set()
        # Appending the first level (all 0's) to the queue and to seen
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    seen.add((r, c))

        # Defining the starting level (which will be the dist to the nearest 0 to be 0)
        level = 0

        # Iterate while queue is non empty
        while queue:
            # Iterate through each cell in a level (we need this since we will keep appending to the queue)
            for level_cell in range(len(queue)):
                # Pop current coordinates from the queue
                r, c = queue.pop(0)
                # Iterate through each neighbour
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # Create need coordinates
                    newR = r + x
                    newC = c + y
                    # Skip over current neighbour if they are out of bounds or already seen
                    if newR < 0 or newR >= rows or newC < 0 or newC >= cols or (newR, newC) in seen:
                        continue
                    # A 1 has been found in a new level, add to queue and seen
                    queue.append((newR, newC))
                    seen.add((newR, newC))
                # set each mat coordinate to be it's cooresponding level (nothing happens for the first level)
                mat[r][c] = level
            # Increment the level
            level += 1
        # Return matrix
        return mat


if __name__ == "__main__":
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(Solution().updateMatrix(mat))

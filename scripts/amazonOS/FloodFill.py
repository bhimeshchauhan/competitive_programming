"""

Flood Fill

https://leetcode.com/problems/flood-fill/

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n

"""


# BFS

from collections import deque
from typing import List


# T/S: O(R*C)
class SolutionBFS:
    def __init__(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.sr = sr
        self.sc = sc
        self.m = len(image)
        self.n = len(image[0])
        self.start_pixel = None
        self.newColor = newColor

    # in bounds and same pixel as our starting pixel
    def is_valid(self, r, c):
        return r in range(self.m) and c in range(self.n) and self.start_pixel == self.image[r][c]

    def floodFill(self):
        self.start_pixel = image[sr][sc]
        # there is no work to be done
        if self.start_pixel == newColor:
            return self.image

        queue = deque([(sr, sc)])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

        while queue:
            r, c = queue.popleft()
            self.image[r][c] = self.newColor

            # try all 4 directions (down, right, up, left)
            for dr, dc in dirs:
                if self.is_valid(r + dr, c + dc):
                    queue.append((r + dr, c + dc))

        return self.image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(SolutionBFS(image, sr, sc, newColor).floodFill())


# DFS
# Time and Space Complexity: O(R*C)

class SolutionDFS:

    def __init__(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.sr = sr
        self.sc = sc
        self.m = len(image)
        self.n = len(image[0])
        self.start_pixel = None
        self.newColor = newColor

    def is_valid(self, r, c):
        return r in range(self.m) and c in range(self.n) and self.start_pixel == self.image[r][c]

    def floodFill(self):
        def dfs(i, j):
            if not self.is_valid(i, j):
                return

            image[i][j] = newColor

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        self.start_pixel = image[sr][sc]
        if self.start_pixel == newColor:
            return image
        dfs(sr, sc)
        return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(SolutionDFS(image, sr, sc, newColor).floodFill())

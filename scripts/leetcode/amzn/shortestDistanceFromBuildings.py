"""

You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. 
You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according 
to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

Example 1:


Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Example 2:

Input: grid = [[1,0]]
Output: 1

Example 3:

Input: grid = [[1]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.

"""

# Approach 1: BFS from Empty Land to All Houses
"""
For each empty cell (grid[i][j] equals 0), start a BFS:
    In the BFS, traverse all 4-directionally adjacent cells that are not blocked or visited and keep track of the distance from the start cell. Each iteration adds 1 to the distance.
    Every time we reach a house, increment houses reached counter housesReached by 1, and increase the total distance distanceSum by the current distance (i.e., the distance from the start cell to the house).
    If housesReached equals totalHouses, then return the total distance.
    Otherwise, the starting cell (and every cell visited during this BFS) cannot reach all of the houses. So set every visited empty land cell equal to 2 so that we do not start a new BFS from that cell and return INT_MAX.

Each time a total distance is returned from a BFS call, update the minimum distance (minDistance).

If it is possible to reach all houses from any empty land cell, then return the minimum distance found. Otherwise, return -1.

"""

# Approach 2: BFS from Houses to Empty Land

"""

For each house cell (grid[i][j] equals 1), start a BFS:
    For each empty cell we reach, increase the cell's sum of distances by the steps taken to reach the cell.
    For each empty cell we reach, also increment the cell's house counter by 1.

After traversing all houses, get the minimum distance from all empty cells which have housesReached equal to totalHouses.

If it is possible for all houses to reach a specific empty land cell, then return the minimum distance found. Otherwise, return -1.

"""

# Approach 3: BFS from Houses to Empty Land (Optimized)

"""

For each grid[i][j] that is equal to 1, start a BFS. During the BFS:
    All 4-directionally adjacent grid cells with values equal to emptyLandValue are valid.
    Visit them one by one and store the distances of these cells from the source in a total matrix.
    Decrease the value of visited cells by 1.

After each BFS traversal, decrement emptyLandValue by 1.

Before we start a BFS call for a house, we set minDist equal to INT_MAX.

Then we will traverse all of the empty land cells with values equal to emptyLandValue

After the last BFS traversal, if the minimum distance equals INT_MAX, then there has not been any cell that can be reached by all the houses, so return -1.

Otherwise, return the minimum distance minDist.


"""
import deque, math

class Solution:
    def shortestDistance(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        total_sum = [[0] * cols for _ in range(rows)]
        
        def bfs(row, col, curr_count):
            min_distance = math.inf
            queue = deque()
            queue.append([row, col, 0])
            while queue:
                curr_row, curr_col, curr_step = queue.popleft()
                for d in dirs:
                    next_row = curr_row + d[0]
                    next_col = curr_col + d[1]
                    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == -curr_count:
                        total_sum[next_row][next_col] += curr_step + 1
                        min_distance = min(min_distance, total_sum[next_row][next_col])
                        grid[next_row][next_col] -= 1
                        queue.append([next_row, next_col, curr_step + 1])
            return min_distance
                
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_distance = bfs(row, col, count)
                    count += 1
                    if min_distance == math.inf:
                        return -1
        
        return min_distance
"""

Shortest Path to Get Food

You are starving and you want to eat food as quickly as possible. 
You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west 
of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. 
If there is no path for you to reach food, return -1.
 

Example 1:


Input: grid = 
[
    ["X","X","X","X","X","X"],
    ["X","*","O","O","O","X"],
    ["X","O","O","#","O","X"],
    ["X","X","X","X","X","X"]
]
Output: 3
Explanation: It takes 3 steps to reach the food.

Example 2:

Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.

Example 3:

Input: grid = 
[
    ["X","X","X","X","X","X","X","X"],
    ["X","*","O","X","O","#","O","X"],
    ["X","O","O","X","O","O","X","X"],
    ["X","O","O","O","O","#","O","X"],
    ["X","X","X","X","X","X","X","X"]
]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.

Example 4:

Input: grid = [["O","*"],["#","O"]]
Output: 2

Example 5:

Input: grid = [["X","*"],["#","X"]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[row][col] is '*', 'X', 'O', or '#'.
The grid contains exactly one '*'.

"""

from collections import deque


def getCurrentPosition(grid, locationMarker='*'):
    """
    Return the row and col coordinates of my location
    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == locationMarker:
                return (row, col)
    return -1


def getGridMarker(location, grid):
    """Return marker in grid at given location"""
    return grid[location[0]][location[1]]


def findValidLocations(location, grid):
    """
    Return all valid locations next to the provided location
    """
    r, c = location
    allDirections = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    
    return [(i, j) for i, j in allDirections
            if 0 <= i < len(grid) and 0 <= j < len(grid[0])
            and getGridMarker((i,j), grid) in ('O', '#')]

    

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        myLocation = getCurrentPosition(grid)
        
        grid[myLocation[0]][myLocation[1]] = -1 # Mark as visted
        
        # Implement a BFS to find food
        queue = deque([(myLocation, 1)])  #  (location, currentSteps)
        
        while queue:
            location, steps = queue.pop()
             
            for adjLocation in findValidLocations(location, grid):
                gridMarker = getGridMarker(adjLocation, grid)
                
                if gridMarker == "#":
                    return steps
                
                grid[adjLocation[0]][adjLocation[1]] = -1 # Mark as visted
                queue.appendleft((adjLocation, steps + 1))
                
        
        return -1
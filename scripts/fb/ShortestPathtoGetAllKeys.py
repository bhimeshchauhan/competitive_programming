"""

Shortest Path to Get All Keys

You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space 
in one of the four cardinal directions. You cannot walk outside the grid, 
or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a 
lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase 
letter of the first k letters of the English alphabet in the grid. This 
means that there is exactly one key for each lock, and one lock for each key; 
and also that the letters used to represent the keys and locks were chosen in 
the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:

Input: grid = ["@.a.#","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.

Example 2:

Input: grid = ["@..aA","..B#.","....b"]
Output: 6

Example 3:

Input: grid = ["@Aa"]
Output: -1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.

"""

'''
w: minimum steps  --> BFS
h: we have additional interesting conditions here 
    we can go to A if we have key a
    then we might need to store more information than just (x,y) in regular graph 
    traversal problem
    
note that for each cell, we can travese more than once since in some cases we need 
to grab the key and then return to a previous place and start searching again. so we should not add the position when we append the position to the queue
'''

# BFS
"""
TimeComplexity: O(MN)
SpaceComplexity: O(MN)
"""

import collections
class Solution:
    def shortestPathAllKeys(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        # 1 . find the start point
        # 2. find how many key we need to collection
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    start = [r, c]
                if grid[r][c] in 'abcdef':
                    cnt += 1

        deque = collections.deque([(start[0], start[1], '')])
        seen = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        steps = 0
        # print(cnt)

        while deque:
            size = len(deque)
            for _ in range(size):
                x, y, key = deque.popleft()
                if (x, y, key) in seen:
                    continue
                if len(key) == cnt:
                    return steps

                seen.add((x, y, key))

                for dx, dy in directions:
                    nx = x+dx
                    ny = y+dy
                    # note that in the following code, we did not
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                        # add the position to seen when we append it to the queue
                        cell = grid[nx][ny]
                        if cell in 'ABCDEF' and cell.lower() in key:
                            deque.append((nx, ny, key))
                        elif cell in '.@':
                            deque.append((nx, ny, key))
                        elif cell in "abcdef":
                            if cell not in key:
                                deque.append((nx, ny, key+cell))
                            else:
                                deque.append((nx, ny, key))

            steps += 1

        return -1

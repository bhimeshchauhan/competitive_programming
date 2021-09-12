"""

Walls and Gates

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent 
INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible 
to reach a gate, it should be filled with INF.

Example 1:

Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]

Example 3:

Input: rooms = [[2147483647]]
Output: [[2147483647]]

Example 4:

Input: rooms = [[0]]
Output: [[0]]

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.

"""

from collections import deque
class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        # base case
        if not rooms:
            return []
        
        R = len(rooms)
        C = len(rooms[0])
        dirxn = [[0,1],[1,0],[0,-1],[-1,0]]
        
        q = deque()
        
        for row in range(R):
            for col in range(C):
                if rooms[row][col] == 0:
                    q.append((row, col))
                    
        while q:
            row, col = q.popleft()
            distance = rooms[row][col]+1
            for dx, dy in dirxn:
                nRow = row + dx
                nCol = col + dy
                if 0 <= nRow < R and 0 <= nCol < C and rooms[nRow][nCol] == 2147483647:
                    rooms[nRow][nCol] = distance
                    q.append((nRow, nCol))
        return rooms
        
        
            
        
        
            


if __name__ == "__main__":
    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    print(Solution().wallsAndGates(rooms))
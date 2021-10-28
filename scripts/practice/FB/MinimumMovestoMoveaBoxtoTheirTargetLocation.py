"""

Minimum Moves to Move a Box to Their Target Location

A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

Example 1:


Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.
Example 2:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1
Example 3:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation:  push the box down, left, left, up and up.
Example 4:

Input: grid = [["#","#","#","#","#","#","#"],
               ["#","S","#",".","B","T","#"],
               ["#","#","#","#","#","#","#"]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid contains only characters '.', '#', 'S', 'T', or 'B'.
There is only one character 'S', 'B', and 'T' in the grid.

"""

"""

Lets break the question into simple parts:

Lets think that we have no person and we have to find the minimum path between box and the target. Easy right? Simple BFS.

If you know how to solve the first part, what I actually do is modify first part with few constraints.

I just check whether the box can be shifted to the new position(up, down, left, right)
For it to be shifted to the new position the person has to be in a corresponding position right?
So we check if the person can travel from his old position to his corresponding new position(using another BFS).
If the person can travel to his new position than the box can be shifted, otherwise the box cannot be shifted.
We keep repeating step 2 until we reach the target or it is not possible to move the box anymore.

NOTE : If you know A* algorithm, you can use Euclidean distance as heuristic and use a priority 
queue instead of normal queue, the worst case time might increase but average case will get better.

"""


class Solution:
    def minPushBox(self, grid):

        # this loop is to get the coordinates of target, box and person. Nothing else is gained here
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "T":
                    target = (i, j)
                if grid[i][j] == "B":
                    box = (i, j)
                if grid[i][j] == "S":
                    person = (i, j)

        # this function checks whether the given coordinates/indices are valid to go
        def valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'

        # this function checks whether the person can travel from current postition to destination position.
        # used simple bfs(dfs can also be used here), should be self explainatory if you know BFS.
        def check(curr, dest, box):
            que = deque([curr])
            v = set()
            while que:
                pos = que.popleft()
                if pos == dest:
                    return True
                new_pos = [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]),
                           (pos[0], pos[1]+1), (pos[0], pos[1]-1)]
                for x, y in new_pos:
                    if valid(x, y) and (x, y) not in v and (x, y) != box:
                        v.add((x, y))
                        que.append((x, y))
            return False

        q = deque([(0, box, person)])
        vis = {box+person}
        # this is the main bfs which gives us the answer
        while q:
            dist, box, person = q.popleft()
            if box == target:  # return the distance if box is at the target
                return dist

            # these are the new possible coordinates/indices box can be placed in (up, down, right, left).
            b_coord = [(box[0]+1, box[1]), (box[0]-1, box[1]),
                       (box[0], box[1]+1), (box[0], box[1]-1)]
            # these are the corresponding coordinates the person has to be in to push .. the box into the new coordinates
            p_coord = [(box[0]-1, box[1]), (box[0]+1, box[1]),
                       (box[0], box[1]-1), (box[0], box[1]+1)]

            for new_box, new_person in zip(b_coord, p_coord):
                # we check if the new box coordinates are valid and our current state is not in vis
                if valid(*new_box) and new_box+box not in vis:
                    # we check corresponding person coordinates are valid and if it is possible for the person to reach the new coordinates
                    if valid(*new_person) and check(person, new_person, box):
                        vis.add(new_box+box)
                        q.append((dist+1, new_box, box))

        return -1

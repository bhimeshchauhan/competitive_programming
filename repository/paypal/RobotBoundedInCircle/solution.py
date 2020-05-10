"""

Intuition:

The idea is to do the traversal as designated and check for two cases
    - if we are back at the initial position [0, 0]
    - if in the end we are in direction other than we started at [ because with enough repetitions we will end
    up in a circle]

"""

class Solution:
    def __init__(self):
        self.Directions = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}

    def isRobotBounded(self, instructions):
        # Clockwise direction
        curr = [0, 0]
        direction = 0

        for move in instructions:
            # If its G we only move ahead in NESW direction
            if move == 'G':
                curr = self.move(curr, direction)
            # Else we take a turn
            else:
                direction = self.turn(move, direction)

        # Id the cur is back at initial index or direction is not same as in the
        # beginning that would menan after enough repitition we would return to same point
        if curr == [0, 0] or direction != 0:
            return True
        else:
            return False

    def move(self, start, direction):
        # North
        if direction == 0:
            start[1] += 1
        # South
        elif direction == 1:
            start[0] += 1
        # East
        elif direction == 2:
            start[1] -= 1
        # West
        else:
            start[0] -= 1

        return start

    def turn(self, move, drection):
        # Turn Right
        if move == 'R':
            drection = (drection + 1) % 4
        # Turn Left
        else:
            drection = (drection - 1) % 4

        return drection

assert Solution().isRobotBounded("GGLLGG")
assert not Solution().isRobotBounded("GG")
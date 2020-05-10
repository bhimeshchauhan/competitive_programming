class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        # Used for moving
        dx, dy = 0, 1
        for i in instructions:
            # move straight
            if i == 'G':
                x, y = x+dx, y+dy
            # For turns we are changing the dx and dy itself
            # turn left
            elif i == 'L':
                dx, dy = -dy, dx
            # turn right
            else:
                dx, dy = dy, -dx
        # return if we are at a start position or our direction is not same
        # the second one means that it would be in same idrection of change in x is 0 and change in y is 1
        return x == y == 0 or not(dx == 0 and dy == 1)

assert Solution().isRobotBounded("GGLLGG")
assert not Solution().isRobotBounded("GG")
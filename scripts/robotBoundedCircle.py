"""

On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of 
three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.

Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.

"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # initial poition
        x = y = 0
        # intially facing north
        direction = 0
        # 0 = north, 1 = east, 2 = south, 3 = west
        # With a move (G) in any direction, you will go 1 unit.
        # So you need to add 1 unit with x or y depending on
        # which direction you are going. For example,
        # if you go north from (x,y), then new position would be
        # (x, y+1) which is you get by x = x+0, y = y+1.
        # Now think about how you can get new position for other direction
        # So creating a dictionary with directions as keys and the
        # amount we need to add with x and y while we go for 1 unit
        # as value. 
        possible_moves = {0: [0,1], 1: [1,0], 2: [0,-1], 3: [-1,0]}
        
        # Now the idea is if after executing the instructions, if you 
        # get your final position at (0,0) or if you are not facing north
        # direction, that means you will be in circle. Not facing north
        # direction means, as you can repeat the instructions, if you are 
        # not facing north after 1st execution of the instructions, just
        # repeat 3 more times of the same instructions, you will see 
        # yourself at the origin. Think about with 'GL' or 'GR' 
        # instructions as an example. With instruction 'GLGR', you 
        # can't be back at origin, no matter how many times you repeat.
        for instruction in instructions:
            # turing left means, you will get the same direction 
            # if you turn right 3 times. modulo beacuse we have 
            # only 4 directions to consider. 
            if instruction == 'L':
                direction = (direction + 3)% 4
            elif instruction == 'R':
                direction = (direction + 1)% 4
            # If we see 'G' means we need to go 1 unit and
            # change x or y value according to the direction 
            # we are going. By this we will get new position. 
            else:
                x = x + possible_moves[direction][0]
                y = y + possible_moves[direction][1]
        # Finally, if you get your final position at (0,0) or if you 
        # are not facing north direction, that means you will be 
        # in circle.
        return (x==0 and y ==0) or direction !=0
                
                
        
        
        
if __name__ == "__main__":
    instructions = "GL"
    print(Solution().isRobotBounded(instructions))
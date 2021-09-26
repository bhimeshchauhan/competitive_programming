"""

Reach a Number

You are standing at position 0 on an infinite number line. 
There is a destination at position target.

You can make some number of moves numMoves so that:

On each move, you can either go left or right.
During the ith move (starting from i == 1 to i == numMoves), 
you take i steps in the chosen direction.
Given the integer target, return the minimum number of moves required 
(i.e., the minimum numMoves) to reach the destination.

Example 1:

Input: target = 2
Output: 3
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to -1 (2 steps).
On the 3rd move, we step from -1 to 2 (3 steps).

Example 2:

Input: target = 3
Output: 2
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to 3 (2 steps).

Constraints:

-109 <= target <= 109
target != 0

"""


class Solution:
    def reachNumber(self, target: int) -> int:
        ans, k = 0, 0
        target = abs(target)
        while ans < target:
            ans += k
            k += 1
        while (ans - target) % 2:
            ans += k
            k += 1
        return k - 1  
    
    
# Binary Search


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        l = 1
        r = target
        
        while l < r:
            mid = l + (r-l) // 2
            if self.enough(mid,target):
                r = mid
            else:
                l = mid+1
        
        steps = l
        
        
        diff = steps * (steps+1) // 2 - target
        if diff % 2:
            steps += steps % 2 + 1
        return steps
        
        
    def enough(self,n,target):
        if n * (n+1) // 2 >= target:
            return True
        return False

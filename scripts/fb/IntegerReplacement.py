"""

Integer Replacement

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:

Input: n = 4
Output: 2

Constraints:

1 <= n <= 231 - 1
"""

"""

A very simple logic, just 4 possible cases:

    if it's an even number - always divide by 2.
    if it's an odd number, 
        we can make it even by either +1 or -1.
            How can we tell? 
                A very simple test. If n+1 % 4 == 0, that means after that we'll be able to divide it by 2 at least twice, 
                so it's worth adding 1. 
        Otherwise, we reduce the number by 1.
    The is an edge case - 3. 
        3 ->4->2->1 is 3 steps while 3->2->1 is 2. 
        So we check that exception before any other odd numbers and force end of the loop by setting n=1 and 
        incrementing c by 1 and then by 1 again.
        
That's it.

"""

class Solution(object):
    def integerReplacement(self, n):
        c = 0        
        while n>1:
            if n==3: return c+2            
            if n%2 == 0: n //= 2
            else: n += -1 if (n+1)%4 else 1
            c += 1        
        return c
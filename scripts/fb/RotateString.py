"""

Rotate String

Given two strings s and goal, return true if and only if 
s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character 
of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" 
after one shift.

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

"""

# Brute Force

"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""


class Solution(object):
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in range(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in range(len(A))):
                return True
        return False


# Simple Check
"""
Time Complexity: O(N^2) where N is the length of A.
Space Complexity: O(N), the space used building A+A.
"""


class Solution(object):
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A+A

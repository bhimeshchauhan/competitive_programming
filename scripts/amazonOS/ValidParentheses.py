"""

Valid Parentheses

https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.

"""

"""
Time Complexity: O(length of the string)
Space Complexity: O(constant with 3 bracket pairs) + O(length of the string)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        bPair = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for brace in s:
            if not stack:
                stack.append(brace)
            elif brace == bPair.get(stack[-1]):
                stack.pop()
            else:
                stack.append(brace)
        return True if not stack else False


if __name__ == '__main__':
    s = "()[]{}"
    assert Solution().isValid(s) == True
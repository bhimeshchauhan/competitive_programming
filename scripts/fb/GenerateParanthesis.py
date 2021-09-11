"""
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8

"""


class Solution(object):
    def generateParenthesis(self, n):
        self.ans = []

        def isValid(arr):
            bal = 0
            for item in arr:
                if item == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        def generate(A=[]):
            if len(A) == 2*n:
                if isValid(A):
                    self.ans.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        generate()
        return self.ans


if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))

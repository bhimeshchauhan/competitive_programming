"""
Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. 
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
such as eval().

Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def calculate(self, s: str) -> int:
        
        # Evaluate
        def evaluate(stack: List, curr: str, operator: str):
            if operator == "-":
                stack.append(-1 * int(curr))
            elif operator == "*":
                n = stack.pop()
                m = int(curr)
                stack.append(n*m)
            elif operator == "/":
                n = stack.pop()
                m = int(curr)
                stack.append(int(n/m))
            else:
                stack.append(int(curr))
            return
        
        stack = []
        operator = ""
        curr = ""
        
        # Make stack
        for char in s:
            if char != ' ':
                if char.isdigit():
                    curr = curr + char
                else:
                    evaluate(stack, curr, operator)    
                    operator = char
                    curr = ""
                    
        # Evaluate last operation
        evaluate(stack, curr, operator)
        
        return sum(stack)
            
                      
        
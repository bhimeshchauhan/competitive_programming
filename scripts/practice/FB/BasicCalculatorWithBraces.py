"""

Basic Calculator III - With Braces

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1+1"
Output: 2

Example 2:

Input: s = "6-4/2"
Output: 4

Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Example 4:

Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
Output: -12

Example 5:

Input: s = "0"
Output: 0

Constraints:

1 <= s <= 104
s consists of digits, '+', '-', '*', '/', '(', and ')'.
s is a valid expression.

"""

class Solution:
    def calculate(self, s: str) -> int:
        operators = {'+', '-', '*', '/'}
        current_number = 0
        operator = '+'
        stack = []
        res = 0
        for i, c in enumerate(s):
            if c.isnumeric():
                current_number = current_number * 10 + int(c)
            if c == '(':
                stack.append(operator)
                operator = '+'
            elif c == ')':
                self.append_result_to_stack(stack, current_number, operator)
                current_number = 0
                # Calculating expression between parentheses
                while stack and stack[-1] not in operators:
                    current_number += stack.pop()
                operator = stack.pop()
            if c in operators or i == len(s) - 1:
                self.append_result_to_stack(stack, current_number, operator)
                operator = c
                current_number = 0
        while stack:
            res += stack.pop()
        return res

    def append_result_to_stack(self, stack, current_number, operator):
        if operator == "+":
            stack.append(current_number)
        elif operator == "-":
            stack.append(-current_number)
        elif operator == "*":
            stack.append(stack.pop() * current_number)
        else:
            div_result = stack.pop() / current_number
            if div_result < 0:
                stack.append(math.ceil(div_result))
            else:
                stack.append(math.floor(div_result))
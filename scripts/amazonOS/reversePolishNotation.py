"""

Evaluate Reverse Polish Notation

https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

"""

# Reducing the List In-place

"""
Time Complexity : O(n^2)
Space Complexity : O(1)
"""




from typing import List
def evalRPN(self, tokens: List[str]) -> int:

    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }

    current_position = 0

    while len(tokens) > 1:

        # Move the current position pointer to the next operator.
        while tokens[current_position] not in "+-*/":
            current_position += 1

        # Extract the operator and numbers from the list.
        operator = tokens[current_position]
        number_1 = int(tokens[current_position - 2])
        number_2 = int(tokens[current_position - 1])

        # Calculate the result to overwrite the operator with.
        operation = operations[operator]
        tokens[current_position] = operation(number_1, number_2)

        # Remove the numbers and move the pointer to the position
        # after the new number we just added.
        tokens.pop(current_position - 2)
        tokens.pop(current_position - 2)
        current_position -= 1

    return tokens[0]


# Evaluate with Stack

"""
Time Complexity : O(n)
Space Complexity : O(n)
"""


def evalRPN(self, tokens: List[str]) -> int:

    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }

    stack = []
    for token in tokens:
        if token in operations:
            number_2 = stack.pop()
            number_1 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_1, number_2))
        else:
            stack.append(int(token))
    return stack.pop()

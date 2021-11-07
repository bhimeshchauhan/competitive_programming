"""

Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example 1:

Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]

Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]

Constraints:

0 <= s.length <= 3 * 104
s consists of digits, '(', ')', and '-' only.

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative stack approach
    def str2tree(self, s):
        # Base case
        if not s:
            return None
        # stack and the number considered currently
        stack, number = [], ''
        # loop the string
        for c in s:
            # if brackets
            if c in '()':
                # if open brackets and has a number
                if c == '(' and number:
                    # add to stack a node with the number
                    stack.append(TreeNode(number))
                    # reset the number
                    number = ''
                # if closed brackets
                elif c == ')':
                    # if has a number
                    if number:
                        # if node in stack and parent
                        node, parent = TreeNode(number), stack[-1]
                        # reset the number
                        number = ''
                    # if no number
                    else:
                        # node and parent are the last two nodes in stack
                        node, parent = stack.pop(), stack[-1]
                    if parent.left:
                        # if we already have left node assign it to right node
                        parent.right = node
                    else:
                        # else add left node first
                        parent.left = node
            # if not brackets
            else:
                number += c
        if number:
            stack = [TreeNode(number)]
        return stack[0]
    
    # Recursive solution
    def str2treeRecur(self, s):
        # handle empty strings
        if not s:
            return None
        
        # handle pure nums
        if s[-1].isdigit():
            return TreeNode(int(s))
        
        # build the root node
        i = s.find('(')
        root = TreeNode(int(s[:i]))
        
        # divide string into left and right children
        stack, j = 1, i
        while stack > 0:
            j += 1
            if s[j] == '(':
                stack += 1
            elif s[j] == ')':
                stack -= 1
        
        # recursively handle the children nodes
        root.left = self.str2treeRecur(s[i+1:j])
        root.right = self.str2treeRecur(s[j+2:-1])
        
        return root

"""

Diameter of Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.dfs(root)

        return self.diameter

    def dfs(self, root):
        if not root:
            return 0

        leftCount = self.dfs(root.left)
        rightCount = self.dfs(root.right)

        self.diameter = max(self.diameter, leftCount + rightCount)

        return max(leftCount, rightCount) + 1

# Without global var


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dd(root)[1]

    def dd(self, root):
        if not root:
            return 0, 0

        depL, diamL = self.dd(root.left)
        depR, diamR = self.dd(root.right)

        dep = 1 + max(depL, depR)
        diam = max(diamL, diamR, depL + depR)

        return dep, diam

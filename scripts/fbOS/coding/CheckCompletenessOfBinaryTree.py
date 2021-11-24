"""

Check Completeness of a Binary Tree

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
import collections


class Solution:
    node_count = 0
    max_position = 0

    def isCompleteTree(self, root):
        self.isCompleteTreeHelper(root, 1)
        return self.max_position == self.node_count

    def isCompleteTreeHelper(self, root, position):
        if root is None:
            return
        self.node_count += 1
        self.max_position = max(self.max_position, position)
        self.isCompleteTreeHelper(root.left, 2 * position)
        self.isCompleteTreeHelper(root.right, 2 * position + 1)


# BFS

# O(n)
# Space: O(n)
def isCompleteTree(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    res = []
    q = collections.deque([(root, 1)])
    while q:
        node, pos = q.popleft()
        res.append(pos)
        if node.left:
            q.append((node.left, 2 * pos))
        if node.right:
            q.append((node.right, 2 * pos + 1))

    return len(res) == res[-1]

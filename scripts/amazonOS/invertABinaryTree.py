"""

Invert a Binary Tree

https://leetcode.com/problems/invert-binary-tree/discuss/2006233/DFS-and-BFS-in-Python

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

# DFS + Recursion
# Time: O(n) Space: O(h)


import collections


def invertTree(self, root):
    if not root:
        return
    tmp = self.invertTree(root.left)
    root.left = self.invertTree(root.right)
    root.right = tmp
    return root

# BFS
# Time: O(n) Space: O(h)


def invertTree(self, root):
    if not root:
        return root
    Q = collections.deque([root])

    while Q:
        for _ in range(len(Q)):
            node = Q.popleft()
            if not node:
                continue

            tmp = node.left
            node.left = node.right
            node.right = tmp

            Q.append(node.left)
            Q.append(node.right)
    return root

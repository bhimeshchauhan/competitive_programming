"""

Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1

"""


# recrusive

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isValidNode(root, float('-inf'), float('inf'))

    def isValidNode(self, root, l, r):
        if not root:
            return True
        return l < root.val < r and self.isValidNode(root.left, l, root.val) and self.isValidNode(root.right, root.val, r)


# recursive


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        order = []
        self.inorderT(root, order)
        for i in range(1, len(order)):
            if order[i] <= order[i-1]:
                return False
        return True

    def inorderT(self, root, order):
        if root is None:
            return
        self.inorderT(root.left, order)
        order.append(root.val)
        self.inorderT(root.right, order)


# iterative


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        order = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            order.append(cur.val)
            cur = cur.right
        print(order)

        for i in range(1, len(order)):
            if order[i] <= order[i-1]:
                return False
        return True

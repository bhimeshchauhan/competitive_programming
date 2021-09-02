"""

Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [2,1]

Example 5:

Input: root = [1,null,2]
Output: [1,2] 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        def inOrder(root):
            if(root == None):
                return

            inOrder(root.left)
            self.res.append(root.val)
            inOrder(root.right)
        
        self.res = []
        inOrder(root)
        return self.res
        
        


# MORRIS ALGO

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
            curr = root
            res = []
            while curr:
                if curr.left:
                    pre = curr.left
                    while pre.right and pre.right!=curr:
                        pre = pre.right
                    if pre.right == curr:
                        pre.right = None
                        res.append(curr.val)
                        curr = curr.right
                    else:
                        pre.right = curr
                        curr = curr.left
                else:
                    res.append(curr.val)
                    curr = curr.right
            return res
        
        
        

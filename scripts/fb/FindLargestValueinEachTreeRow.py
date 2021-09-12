"""

Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:

Input: root = [1,2,3]
Output: [1,3]

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,null,2]
Output: [1,2]

Example 5:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, idx=0):
            
            if not node:
                return
            
            # condition to satisfy
            if len(res) > idx:
                res[idx] = max(res[idx], node.val)
            else:
                res.append(node.val)
            
            traverse(node.left, idx+1)
            traverse(node.right, idx+1)
        res = []
        traverse(root)
        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, str_res=''):
            if node:
                str_res += str(node.val)
                if not node.left and not node.right:
                    res.append(str_res)
                else:
                    str_res += '->'
                    dfs(node.left, str_res)
                    dfs(node.right, str_res)
        dfs(root)
        return res
        
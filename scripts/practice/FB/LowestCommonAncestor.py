"""



"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def recurse(node):
            if not node:
                return False
            
            left = recurse(node.left)
            right = recurse(node.right)
            
            mid = node == p or node == q
            print(node.val, mid+left+right)
            
            if mid+left+right >= 2:
                self.ans = node
                
            return mid or left or right
        
        recurse(root)
        return self.ans
    


def lowestCommonAncestor(self, root, p, q):
        if root == None or root == p or root == q:
            return root
        
		# Find p/q in left subtree
        l = self.lowestCommonAncestor(root.left, p, q)
		
		# Find p/q in right subtree
        r = self.lowestCommonAncestor(root.right, p, q)
        
		# If p and q found in left and right subtree of this node, then this node is LCA
        if l and r:
            return root
        
		# Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
        return l if l else r
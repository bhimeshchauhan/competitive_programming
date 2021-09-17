"""

Invert Binary Tree



"""

# DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root:
            # General case:
            
            # invert child node of current root
            root.left, root.right = root.right, root.left
            
            # invert subtree with DFS
            
            if root.left:
                self.invertTree( root.left )
            
            if root.right:
                self.invertTree( root.right )
            
            return root
        
        else:
            # Base case:
            # empty tree
            
            return None
        

# BFS

from collections import deque    
    
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:        
        
        traversal_queue = deque([root]) if root else None
        
		# lanuch BFS, aka level-order-traversal to carry out invertion
        while traversal_queue:
            
            cur_node = traversal_queue.popleft()
            
			# Invert child node of current node
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            
			# push left child into queue to invert left subtree
            if cur_node.left:
                traversal_queue.append( cur_node.left )
            
			# push right child into queue to invert right subtree
            if cur_node.right:
                traversal_queue.append( cur_node.right )                
        
        return root
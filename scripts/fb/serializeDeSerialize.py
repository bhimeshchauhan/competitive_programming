# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.string = ""
        def dfs(root):
            if root:
                self.string += str(root.val) + ','
                dfs(root.left)
                dfs(root.right)
            else:
                self.string += 'None,'

        dfs(root)
        print(self.string[:-1])
        return self.string[:-1]
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        def dfs(arr):
            if arr[0] == 'None':
                arr.pop(0)
                return None
            
            root = TreeNode(arr[0])
            arr.pop(0)
            root.left = dfs(arr)
            root.right = dfs(arr)
            return root
        
        arr = data.split(',')
        root = dfs(arr)
        return root
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
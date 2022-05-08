"""


"""

# DFS

"""
Time: O(N)
Space: O(N)
"""

# Definition for a binary tree node.




from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preorder_encode(node):

            if not node:
                output.append('N')
                return

            output.append(str(node.val))
            preorder_encode(node.left)
            preorder_encode(node.right)

        output = []
        preorder_encode(root)

        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def preorder_decode():

            if data[self.curr_idx] == 'N':
                self.curr_idx += 1
                return

            node = TreeNode(int(data[self.curr_idx]))
            self.curr_idx += 1
            node.left = preorder_decode()
            node.right = preorder_decode()

            return node

        data = data.split(",")
        self.curr_idx, n = 0, len(data)

        return preorder_decode()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# BFS

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if node is None:
                vals.append("x")
                continue

            vals.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        vals = data.split(",")
        nodes = iter((None if v == 'x' else TreeNode(int(v))) for v in vals)
        root = next(nodes)
        q = deque([root])

        while q:
            node = q.popleft()

            left = next(nodes)
            if left:
                node.left = left
                q.append(left)

            right = next(nodes)
            if right:
                node.right = right
                q.append(right)

        return root

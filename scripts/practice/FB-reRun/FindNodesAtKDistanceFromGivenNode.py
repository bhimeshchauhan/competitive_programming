"""

All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:

Input: root = [1], target = 1, k = 3
Output: []

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(
            self, root: TreeNode, target: TreeNode, K: int) -> list[int]:
        def set_parents(root: TreeNode, parent: TreeNode) -> None:
            if root:
                root.parent = parent
                set_parents(root.left, root)
                set_parents(root.right, root)

        set_parents(root, None)
        currNodes = [target]
        visited = {target}
        for _ in range(K):
            nextNodes = []
            for currNode in currNodes:
                for node in [currNode.left, currNode.right, currNode.parent]:
                    if node and node not in visited:
                        visited.add(node)
                        nextNodes.append(node)

            currNodes = nextNodes

        return [node.val for node in currNodes]
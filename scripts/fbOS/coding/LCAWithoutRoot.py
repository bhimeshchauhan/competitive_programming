"""

Lowest Common Ancestor of a Binary Tree III

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node'):

        if not p:
            return q
        if not q:
            return p

        root = None
        root = q
        while root.parent:
            root = root.parent

        def lca(root, p, q):
            if not root:
                return

            if root is p or root is q:
                return root

            left = right = None
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            if left and right:
                return root
            return left or right

        return lca(root, p, q)

# Definition for a Node.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p, q):

        # # balance distance from root
        # calculate heights
        curr_p, curr_q = p, q
        height_p, height_q = 0, 0
        while curr_p.parent is not None or curr_q.parent is not None:
            if curr_p.parent is not None:
                height_p += 1
                curr_p = curr_p.parent
            if curr_q.parent is not None:
                height_q += 1
                curr_q = curr_q.parent

        # two should be the lower one
        one, two = p, q
        if height_p > height_q:
            one, two = q, p

        # move two up
        for _ in range(abs(height_p-height_q)):
            two = two.parent

        # # find common ancestor
        while one != two:
            one = one.parent
            two = two.parent

        return one

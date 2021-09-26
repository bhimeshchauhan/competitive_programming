"""

Binary Tree Cameras

You are given the root of a binary tree. We install cameras on 
the tree nodes where each camera at a node can monitor its parent, 
itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes 
of the tree.

Example 1:

Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. 
The above image shows one of the valid configurations of camera placement. 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val == 0

"""

# DFS

"""

One of the first realizations that we can make is that we never need to 
place a camera on a leaf, since it would always be better to place a 
camera on the node above a leaf. This should lead us to thinking that 
we need to start from the bottom of the binary tree and work our way up.

This naturally calls for a depth first search (DFS) approach with a 
recursive helper function (dfs). We can navigate to the lowest part of 
the tree, then deal with placing cameras on the way back up the recursion 
stack, using the return values to pass information from child to parent.

First, we should consider the different information that will be necessary
to pass up to the parent about the child node, and in fact there are only three:

- Nothing below needs monitoring.
- A camera was placed below and can monitor the parent.
- An unmonitored node below needs a camera placed above.

The next challenge is to identify the different scenarios 
that we'll face once we've collected the values (val) of the 
children of the current node. Again, there are three scenarios:

- No child needs monitoring, so hold off on placing a camera and 
instead return a value that indicates that the parent will have 
to place one.
- One or more of the chidren need monitoring, so we will have 
to place a camera here. We'll want to return a value indicating 
that the parent will be monitored.
- One of the children has a camera and the other child either 
has a camera or doesn't need monitoring (otherwise we would trigger 
the second scenario instead). This tree is fully monitored, but has 
no monitoring to provide to the parent; it will return the same value 
as a null branch.

With all this in mind, we can let the return value indicate how we move
from one state to another. At each node if the combined val from below 
is greater than 2, then we need to place a camera. If so we should increment 
our counter (ans) before moving on.

One last tricky piece is the root node. If the root node returns a value 
indicating that it still needs a camera, we should add 1 to ans before we 
return it.

"""

"""
Time Complexity: O(N) where N is the number of nodes in the binary tree
Space Complexity: O(M) where M is the maximum depth of the binary tree, 
which can range up to N, for the recursion stack
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ans = 0
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node: return 0
            val = dfs(node.left) + dfs(node.right)
            if val == 0: return 3
            if val < 3: return 0
            self.ans += 1
            return 1
        return self.ans + 1 if dfs(root) > 2 else self.ans
"""

Maximum Sum BST in Binary Tree

Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 2:

Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.

Example 4:

Input: root = [2,1,3]
Output: 6

Example 5:

Input: root = [5,4,8,3,null,6,3]
Output: 7

Constraints:

The number of nodes in the tree is in the range [1, 4 * 104].
-4 * 104 <= Node.val <= 4 * 104

"""


"""

Most solutions discussed here solve this using Post Order traversal. 
I tried to solve this using preorder traversal (using the floor and ceiling method to check validity of 
BST like in here), and got confused.

For this problem we need to build the solution from the bottom-up i.e., 
from the leaf nodes towards the root. Only then can we check if the current sub-tree is a valid BST, 
and then update the maximum sum. This means post order is the ideal way to traverse the tree.

Here's a solution using this idea:

"""

class Solution:
    def __init__(self):
        self.maxSum = 0
        
    def maxSumBST(self, root):
        def postOrderTraverse(node):
            """ 
            Perform post order traversal of tree
            to determine sub trees which are BSTs
            and calculate maximum sum of its elements.
            
            Returns:
            isValidBST: True if valid BST else False
            currentSum: sum of current sub tree. None 
                        if not a valid BST.
            currentMin: minimum value of current sub tree
            currentMax: maximum value of current sub tree
            """
            if not node:
                return True, 0, float('inf'), float('-inf') # Empty sub tree

            lValidBST, lSum, lMin, lMax = postOrderTraverse(node.left)
            rValidBST, rSum, rMin, rMax = postOrderTraverse(node.right)

            # Check if current subtree is a valid BST
            if lValidBST and rValidBST and lMax < node.val < rMin: 
                currSum = lSum + rSum + node.val
                currMin = lMin if lMin != float('inf') else node.val
                currMax = rMax if rMax != float('-inf') else node.val
                self.maxSum = max(self.maxSum, currSum)  # update max sum
                return True, currSum, currMin, currMax
            
            return False, None, None, None 
        
        postOrderTraverse(root)
        return self.maxSum

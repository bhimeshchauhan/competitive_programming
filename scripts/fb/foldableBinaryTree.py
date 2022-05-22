"""

1) If tree is empty, then return true.
2) Convert the left subtree to its mirror image
    mirror(root->left); /* See this post */
3) Check if the structure of left subtree and right subtree is same
   and store the result.
    res = isStructSame(root->left, root->right); /*isStructSame()
        recursively compares structures of two subtrees and returns
        true if structures are same */
4) Revert the changes made in step (2) to get the original tree.
    mirror(root->left);
5) Return result res stored in step 2.



"""

# Python3 program to check foldable binary tree

# A binary tree node has data,
# pointer to left child and a
# pointer to right child


class newNode:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Returns true if the given
# tree is foldable


def isFoldable(node):

    # base case
    if node == None:
        return True

    # convert left subtree to its mirror
    mirror(node.left)

    # Compare the structures of the right subtree and mirrored
    # left subtree
    res = isStructSame(node.left, node.right)

    # Get the original tree back
    mirror(node.left)

    return res


def isStructSame(a, b):

    if a == None and b == None:
        return True
    if a != None and b != None and isStructSame(a.left, b.left) and isStructSame(a.right, b.right):
        return True

    return False


def mirror(node):

    if node == None:
        return
    else:

        # do the subtrees
        mirror(node.left)
        mirror(node.right)

        # swap the pointers in this node
        temp = node.left
        node.left = node.right
        node.right = temp


# Driver Code
if __name__ == '__main__':

    '''
    The constructed binary tree is
                    1
            / \
            2	 3
            \ /
                    4 5
    '''
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.right.left = newNode(4)
    root.left.right = newNode(5)

    if isFoldable(root):
        print("tree is foldable")
    else:
        print("Tree is not foldable")



"""

Check if Left and Right subtrees are Mirror

There are mainly two functions:
// Checks if tree can be folded or not 

IsFoldable(root)
1) If tree is empty then return true
2) Else check if left and right subtrees are structure wise mirrors of
    each other. Use utility function IsFoldableUtil(root->left,
    root->right) for this.
// Checks if n1 and n2 are mirror of each other. 

IsFoldableUtil(n1, n2)
1) If both trees are empty then return true.
2) If one of them is empty and other is not then return false.
3) Return true if following conditions are met
   a) n1->left is mirror of n2->right
   b) n1->right is mirror of n2->left

"""

# Python3 program to check
# foldable binary tree

# Utility function to create a new
# tree node


class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

# Returns true if the given tree can be folded


def IsFoldable(root):
	if (root == None):
		return True
	return IsFoldableUtil(root.left, root.right)


# A utility function that checks
# if trees with roots as n1 and n2
# are mirror of each other
def IsFoldableUtil(n1, n2):
	# If both left and right subtrees are NULL,
	# then return true
	if n1 == None and n2 == None:
		return True

	# If one of the trees is NULL and other is not,
	# then return false
	if n1 == None or n2 == None:
		return False

	# Otherwise check if left and
	# right subtrees are mirrors of
	# their counterparts
	
	d1 = IsFoldableUtil(n1.left, n2.right)
	d2 = IsFoldableUtil(n1.right, n2.left)
	return d1 and d2


# Driver code
if __name__ == "__main__":

	""" The constructed binary tree is
	1
	/ \
	2 3
	\ /
	4 5
"""
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.right = newNode(4)
	root.right.left = newNode(5)

	if IsFoldable(root):
		print("Tree is foldable")
	else:
		print("Tree is not foldable")


"""

Iterative Approach: The idea is to use Queue for traversing the tree and using the BFS approach. 

In order to prove it is a foldable tree, we need to check two conditions whether null or not.

The left child of the left subtree = the right child of the right subtree. Both of them should be not null.
The right child of left subtree = left child of right subtree. Both of them should be null or not null.


"""

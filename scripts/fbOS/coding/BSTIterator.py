"""

Binary Search Tree Iterator

Implement the BSTIterator class 
that represents an iterator over 
the in-order traversal of a binary 
search tree (BST):

BSTIterator(TreeNode root) Initializes 
an object of the BSTIterator class. 
The root of the BST is given as part 
of the constructor. The pointer should 
be initialized to a non-existent number 
smaller than any element in the BST.

boolean hasNext() Returns true if 
there exists a number in the traversal 
to the right of the pointer, otherwise 
returns false.

int next() Moves the pointer to the right, 
then returns the number at the pointer.

Notice that by initializing the pointer 
to a non-existent smallest number, the 
first call to next() will return the 
smallest element in the BST.

You may assume that next() calls will always
be valid. That is, there will be at least 
a next number in the in-order traversal 
when next() is called.

Example 1:

Input

["BSTIterator", "next", "next", "hasNext", 
"next", "hasNext", "next", "hasNext", "next", 
"hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], 
[], [], [], [], [], []]

Output

[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation

BSTIterator bSTIterator = 
new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

Constraints:

The number of nodes in the tree 
is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to 
hasNext, and next.
 

Follow up:

Could you implement next() and hasNext() 
to run in average O(1) time and use O(h) 
memory, where h is the height of the tree?

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None,
                 right=None):
        self.val = val
        self.left = left
        self.right = right


"""

Time complexity : O(N) is the time taken by 
the constructor for the iterator. The problem 
statement only asks us to analyze the complexity 
of the two functions, however, when implementing 
a class, it's important to also note the time it 
takes to initialize a new object of the class and 
in this case it would be linear in terms of the 
number of nodes in the BST. In addition to the 
space occupied by the new array we initialized, 
the recursion stack for the inorder traversal 
also occupies space but that is limited to O(h) 
where hh is the height of the tree.

next() would take O(1)
hasNext() would take O(1)

Space complexity : O(N) since we create a new 
array to contain all the nodes of the BST. 
This doesn't comply with the requirement 
specified in the problem statement that the 
maximum space complexity of either of the 
functions should be O(h) where hh is the 
height of the tree and for a well balanced 
BST, the height is usually logN. So, we get 
great time complexities but we had to compromise 
on the space. Note that the new array is 
used for both the function calls and hence 
the space complexity for both the calls is O(N).

"""


class BSTIterator:

    def __init__(self, root):
        # Array containing all the nodes
        # in the sorted order
        self.nodes_sorted = []

        # Pointer to the next smallest
        # element in the BST
        self.index = -1

        # Call to flatten the input binary
        # search tree
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self):
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self):
        return self.index + 1 < \
            len(self.nodes_sorted)

# Controlled Recursion

"""
Time complexity : The time complexity for 
this approach is very interesting to analyze. 
Let's look at the complexities for both the 
functions in the class:

hasNext is the easier of the lot since all we
do in this is to return true if there are any 
elements left in the stack. Otherwise, we return 
false. So clearly, this is an O(1) operation 
every time. Let's look at the more complicated 
function now to see if we satisfy all the 
requirements in the problem statement

next involves two major operations. One is 
where we pop an element from the stack which 
becomes the next smallest element to return. 
This is a O(1) operation. However, we then 
make a call to our helper function 
_inorder_left which iterates over a 
bunch of nodes. This is clearly a linear 
time operation i.e. O(N) in the worst case. 
This is true.

However, the important thing to note 
here is that we only make such a call 
for nodes which have a right child. 
Otherwise, we simply return. Also, even if 
we end up calling the helper function, 
it won't always process N nodes. They will 
be much lesser. Only if we have a skewed tree 
would there be N nodes for the root. But that 
is the only node for which we would call the 
helper function.

Thus, the amortized (average) time complexity
for this function would still be O(1) which 
is what the question asks for. We don't need 
to have a solution which gives constant time 
operations for every call. We need that 
complexity on average and that is what we get.

Space complexity: The space complexity is O(N) 
(N is the number of nodes in the tree), 
which is occupied by our custom stack for 
simulating the inorder traversal. Again, we 
satisfy the space requirements as well as 
specified in the problem statement.

"""

class BSTIterator:

    def __init__(self, root: TreeNode):

        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm 
        # starts with a call to the helper 
        # function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):

        # For a given node, add all 
        # the elements in the leftmost 
        # branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        """

        # Node at the top of the stack is 
        # the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If 
        # the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(
                topmost_node.right)
        return topmost_node.val

    def hasNext(self):
        """
        @return whether we have a next 
        smallest number
        """
        return len(self.stack) > 0
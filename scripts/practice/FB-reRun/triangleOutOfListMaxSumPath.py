"""

Triangle of list max path sum 

"""

"""

A correct pseudo solution:

- Obtain all top-to-bottom path sums and store them in a hash table as keys. 
While doing so, as you traverse at each level, add the direction turned; 
"L" or "R" to the corresponding value in the hashtable.

-> Utilizing above example:

- Starting at 1, we can go down and find 4 paths: 1->3->8 (left, left), 
1->3->10(left, right), 1->5->10(right, left) and 1->5->4 (right, right)
- We add the sum of each path (12, 14, 16, 10) to a hashtable as the key 
and its corresponding turns (LL, LR, RL, RR) as the value. In other words, 
we get: {12: "LL", 14: "LR", 16: "RL", 10: "RR"}.

Compare the results at the end and return the value for the highest key.

- 16>14>12>10, 16 is our maximum path sum and its' key is "RL" so that's our answer.


"""

"""Time: O(n^2) due to double iteration and O(n) space due to res."""


class Solution(object):
    def maximumTotal(self, triangle):
        # edge case
        if not triangle:
            return
            # init return value (O(n) space)
        res = triangle[-1]
        # enter and iterate the list of lists using double for loop, (this nested loop is the cause of O(n^2) time)
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = max(res[j], res[j+1]) + triangle[i][j]
        return res[0]

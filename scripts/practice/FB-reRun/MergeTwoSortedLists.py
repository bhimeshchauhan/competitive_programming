"""

Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
2 -> 5 -> 6
1 -> 1 -> 3 -> 4 -> 6
"""
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            print('l1', l1)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            print('l2', l2)
            return l2
        
                
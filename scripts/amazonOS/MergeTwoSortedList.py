"""

Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.


"""

"""
Time: O(n)
Space: O(1)
"""




from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __bool__(self):
        """Return bool(self)."""
        return self.next is not None


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(4)
    l1.next = l1_2
    l1_2.next = l1_3

    l2 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2.next = l1_2
    l2_2.next = l1_3
    print(mergeTwoLists(l1, l2).__bool__())

"""

Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

"""

# Brute Force

"""

Intuition & Algorithm

- Traverse all the linked lists and collect the values of the nodes into an array.
- Sort and iterate over this array to get the proper value of nodes.
- Create a new sorted linked list and extend it with the new nodes.

"""

"""

Complexity Analysis
Time complexity : O(NlogN) where N is the total number of nodes.

Collecting all the values costs O(N) time.
A stable sorting algorithm costs O(NlogN) time.
Iterating for creating the linked list costs O(N) time.

Space complexity : O(N).

Sorting cost O(N) space (depends on the algorithm you choose).
Creating a new linked list costs O(N) space.

"""

from queue import PriorityQueue
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


# Compare one by one By Priority Queue

"""

Complexity Analysis

Time complexity : O(Nlogk) where k is the number of linked lists.

The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. 
But finding the node with the smallest value just costs O(1) time.
There are N nodes in the final linked list.

Space complexity :

O(n) Creating a new linked list costs O(n) space.
O(k) The code above present applies in-place method 
which cost O(1) space. And the priority queue 
(often implemented with heaps) costs O(k) 
space (it's far less than N in most situations).

"""

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


# Merge with Divide And Conquer
"""

Intuition & Algorithm

- This approach walks alongside the one above but is improved a lot. 
We don't need to traverse most nodes many times repeatedly

Pair up k lists and merge each pair.

After the first pairing, k lists are merged into k/2 
lists with average 2N/k length, then k/4, k/8 and so on.

Repeat this procedure until we get the final sorted linked list.

"""

"""

Complexity Analysis

Time complexity : O(Nlogk) where k is the number of linked lists.

We can merge two sorted linked list in O(n) time where nn is the total number of nodes in two lists.
Sum up the merge process and we can get: O(Nlogk)

Space complexity : O(1)

We can merge two sorted linked lists in O(1) space.

"""


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

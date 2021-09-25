"""

Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?

"""

# Reverse Input + Construct Output by Adding to Front


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            # keep the next node
            tmp = head.next
            # reverse the link
            head.next = last
            # update the last node and the current node
            last = head
            head = tmp

        return last

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # reverse lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        head = None
        carry = 0
        while l1 or l2:
            # get the current values
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0

            # current sum and carry
            val = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10

            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head


# Follow Up: Do not Reverse Input.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next
            n1 += 1
        while curr2:
            curr2 = curr2.next
            n2 += 1

        # parse both lists
        # and sum the corresponding positions
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            if n1 < n2:
                val += curr2.val
                curr2 = curr2.next
                n2 -= 1

            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

        # take the carry into account
        # to have all elements to be less than 10
        # 10->10->3 --> 0->1->4 --> 4->1->0
        curr1, head = head, None
        carry = 0
        while curr1:
            # current sum and carry
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10

            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the list
            curr1 = curr1.next

        # add the last carry
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head

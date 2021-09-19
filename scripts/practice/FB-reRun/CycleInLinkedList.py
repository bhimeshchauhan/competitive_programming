"""

Cycle In LinkedList

"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
            
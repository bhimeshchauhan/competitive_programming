"""

Design Front Middle Back Queue

Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:

FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
Notice that when there are two middle position choices, the operation is 
performed on the frontmost middle position choice. For example:

Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
 

Example 1:

Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", 
"pushMiddle", "pushMiddle", "popFront", "popMiddle", 
"popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
 

Constraints:

1 <= val <= 109
At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.

"""

# Two Deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def _correct_size(self):
        while len(self.back) > len(self.front):
            self.front.append(self.back.popleft())

        while len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._correct_size()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)
        self._correct_size()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._correct_size()

    def popFront(self) -> int:
        front = self.front if self.front else self.back
        ret = front.popleft() if front else -1
        self._correct_size()
        return ret

    def popMiddle(self) -> int:
        ret = self.front.pop() if self.front else -1
        self._correct_size()
        return ret

    def popBack(self) -> int:
        back = self.back if self.back else self.front
        ret = back.pop() if back else -1
        self._correct_size()
        return ret


# Using DLL

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class FrontMiddleBackQueue:

    def __init__(self):
        self.head = None
        self.last = None

    def pushFront(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            self.last = node
            node.next = node
            node.prev = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.last.next = self.head

    def pushMiddle(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            self.last = node
            node.next = node
            node.prev = node
            return
        if self.head.next == self.head:
            node.next = self.head
            node.prev = self.last
            self.head.prev = node
            self.head = node
            self.last.next = self.head
            return
        front = self.head
        last = self.last
        while front != last and front.next != last:
            front = front.next
            last = last.prev
        if front == last:
            front = front.prev
        front.next = node
        node.prev = front
        node.next = last
        last.prev = node

    def pushBack(self, val: int) -> None:
        node = Node(val)
        if self.last == None:
            self.head = node
            self.last = node
            node.next = node
            node.prev = node
        else:
            node.next = self.head
            node.prev = self.last
            self.last.next = node
            self.last = node
            self.head.prev = self.last

    def popFront(self) -> int:
        if self.head == None:
            return -1
        val = self.head.val
        if self.head.next == self.head:
            self.head = None
            self.last = None
            return val
        self.head = self.head.next
        self.last.next = self.head
        self.head.prev = self.last
        return val

    def popMiddle(self) -> int:
        if self.head == None:
            return -1
        if self.head.next == self.head:
            val = self.head.val
            self.head = None
            self.last = None
            return val
        front = self.head
        last = self.last
        while front != last and front.next != last:
            front = front.next
            last = last.prev
        val = front.val
        if front == last:
            last = last.next
        if front == self.head:
            front = front.next
            self.head = front
            front.prev = self.last
            self.last.next = self.head
        else:
            front = front.prev
            front.next = last
            last.prev = front
        return val

    def popBack(self) -> int:
        if self.last == None:
            return -1
        val = self.last.val
        if self.last.next == self.last:
            self.head = None
            self.last = None
            return val
        self.last = self.last.prev
        self.last.next = self.head
        self.head.prev = self.last
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

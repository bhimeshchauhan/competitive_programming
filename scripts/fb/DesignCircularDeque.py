"""

Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.

"""

class MyCircularDeque:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.size = k
        self.arr  = [None]*k  # O(n) initialization
        # self.arr = {} #  O(1) initialization (completes full O(1) code)
        self.head = self.tail = None
        self.busy = 0
    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.head is None:
            self.head = self.tail = 0
        else:
            new = (self.head+1)%self.size
            if new == self.tail:
                return False
            self.head = new
        self.arr[self.head] = value
        self.busy += 1
        return True
    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.tail is None:
            self.head = self.tail = 0
        else:
            new = (self.tail-1)%self.size
            if new == self.head:
                return False
            self.tail = new
        self.arr[self.tail] = value
        self.busy += 1
        return True
    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.head is None:
            return False
        self.arr[self.head] = None
        self.busy -= 1
        if self.tail==self.head:
            self.head = self.tail = None
        else:
            self.head = (self.head-1)%self.size
        return True
    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.tail is None:
            return False
        self.arr[self.tail] = None
        self.busy -= 1
        if self.tail==self.head:
            self.head = self.tail = None
        else:
            self.tail = (self.tail+1)%self.size
        return True
    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.head is None:
            return -1
        return self.arr[self.head]
    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.tail is None:
            return -1
        return self.arr[self.tail]
    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.head is None
    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.busy == self.size
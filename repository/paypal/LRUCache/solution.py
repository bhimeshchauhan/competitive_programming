"""
1. Set the capacity and initialize an ordered dictionary
2. for get first get the value and then move it to the end
3. for put first check if the value exists and then delete and assign it to the dic again otherwise
just add the value also evict the first item in dic if more in capacity
"""
"""
Doubly Linked List implementation
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.dic = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic.get(key)
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        newNode = Node(key, value)
        self.add(newNode)
        self.dic[key] = newNode
        if len(self.dic) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dic[node.key]

    def remove(self, node):
        pre = node.prev
        ne = node.next
        pre.next = ne
        ne.prev = pre

    def add(self, node):
        pre = self.tail.prev
        pre.next = node
        node.prev = pre
        node.next = self.tail
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache( 2 )
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
# Distributed Cache

---
---

## Problem Statement

We need to cache data on a distributed system. The data should be stored in a cache server and distributed to other servers.

## Functional Requirements

- put (key, value)
- get (key)

## Non Functional Requirements

- Scalable - Scales out easily together with increasing number of requests and data
- High Availability - If one server fails, the data is still available.
- High Performance - Fast puts and Fast gets

## High Level Design

### Local Cache

- Data Structure : Hash Table
- Eviction Policy :
  - Least Recently Used
  - Most Frequently Used
- To track evict policy:
  - To track LRU:
    - DLL ( Doubly Linked List )

- GET
  - Is item in Cache?
    - If yes, return value
    - If no, return null

- PUT
  - Is item in Cache?
    - If yes, update value and move to front of DLL
    - If no
      - Is cache full?
        - If yes,
          - evict LRU item from both DLL and Hash Table
          - add new item to front of DLL
          - add new item to Hash Table
        - If no,
          - add item to front of DLL
          - add item to Hash Table


## LRU Cache Implementation

```python
class DLLNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = {}
        self.head = DLLNode(None, None)
        self.tail = DLLNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.hash_table:
        node = self.hash_table[key]
        self._remove(node)
        self._add(node)
        return node.value
        return None
    
    def put(self, key, value):
        if key in self.hash_table:
        node = self.hash_table[key]
        node.value = value
        self._remove(node)
        self._add(node)
        else:
        node = DLLNode(key, value)
        if len(self.hash_table) == self.capacity:
            self._remove(self.tail.prev)
            del self.hash_table[self.tail.prev.key]
        self._add(node)
        self.hash_table[key] = node
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
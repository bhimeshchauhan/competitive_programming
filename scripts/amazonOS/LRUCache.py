"""

Least Recently Used Cache

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"

Output: [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
]

Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.

"""

"""

Question
- What is input? What is output format?
- What happens when the key is already present?
- What happens when the key is present and different value is given?
- What happens when the key is present and same value is given?

"""

# Doubly Linked List
class ListNode():
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    """
    approach: 
    we can solve this problem using a doubly linked list and a hash map
    to get and put the values in O(1) time
    Doubly linked list will contain the head as the most recently used value
    and tail will contain the least recently used item
    
    put operation:
    if new key is added, it will be added to the front of list
    if new key is added but capacity is full, tail node will be deleted first to make room
    and then new node will be added in front
    if key value is updated, then value is updated and then reposition will happend such that
    the updated node is moved to the front of the list and rest all are pushed one step down
    
    get operation:
    if key is present, reposition that key to front of list and return the value
    else return -1
    
    This blogpost has a good explanation for the LRU cache mechanism, we can implmenent based
    on that
    https://www.interviewcake.com/concept/java/lru-cache#:~:text=LRU%20caches%20store%20items%20in,)%20O(1)%20time.
    """

    def __init__(self, capacity: int):
        self.hash_map = {}
        self.head = self.tail = None
        self.capacity = capacity

    def _reposition(self, key):
        temp = self.hash_map[key]
        if self.head != temp:
            temp.prev.next = temp.next
            if temp != self.tail:
                temp.next.prev = temp.prev
            else:
                self.tail = self.tail.prev
                
            temp.next = self.head
            temp.prev = None
            self.head.prev = temp
            self.head = temp
        # print('after reposition, head_key={}, tail_key={}'.format(self.head.key, self.tail.key)) 
        
            
    def get(self, key: int) -> int:
        if key in self.hash_map:
            self._reposition(key)
            return self.hash_map[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            # update the value of key
            self.hash_map[key].val= value
            # reposition the node to be the most recently used
            self._reposition(key)
        else:
            # if key is not existing, check the capacity first
            if len(self.hash_map) == self.capacity:
                # capacity is full, delete the least recently used and add to the front the new key
                # remove the last node
                del self.hash_map[self.tail.key]
                if self.tail == self.head:
                    self.tail = self.head = None
                    node = ListNode(key, value, None, self.head)
                    self.hash_map[key] = node
                    self.tail = self.head = node
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    # create a new node for new key
                    node = ListNode(key, value, None, self.head)
                    # add the key to hash map
                    # add the new node to front of list
                    self.hash_map[key] = node
                    self.head.prev = node
                    self.head = node
                    # print('head_key={}, tail_key={}'.format(self.head.key, self.tail.key))
                    # print(self.hash_map)
            else:
                # create a new node and add it to front of list. 
                # also add it to hash_map
                node = ListNode(key, value, None, self.head)
                if len(self.hash_map) == 0:
                    # first node is added
                    self.head = self.tail = node
                else:
                    self.head.prev = node
                    self.head = node
                self.hash_map[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
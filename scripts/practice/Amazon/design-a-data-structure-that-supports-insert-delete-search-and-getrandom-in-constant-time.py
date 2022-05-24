"""

Design a data structure that supports insert, delete, search and getRandom in constant time

We can use hashing to support first 3 operations in Θ(1) time. How to do the 4th operation? The idea is to use a resizable array (ArrayList in Java, vector in C) together with hashing. Resizable arrays support insert in Θ(1) amortized time complexity. To implement getRandom(), we can simply pick a random number from 0 to size-1 (size is the number of current elements) and return the element at that index. The hash map stores array values as keys and array indexes as values.
Following are detailed operations.
insert(x) 
1) Check if x is already present by doing a hash map lookup. 
2) If not present, then insert it at the end of the array. 
3) Add in the hash table also, x is added as key and last array index as the index.
remove(x) 
1) Check if x is present by doing a hash map lookup. 
2) If present, then find its index and remove it from a hash map. 
3) Swap the last element with this element in an array and remove the last element. 
Swapping is done because the last element can be removed in O(1) time. 
4) Update index of the last element in a hash map.
getRandom() 
1) Generate a random number from 0 to last index. 
2) Return the array element at the randomly generated index.
search(x) 
Do a lookup for x in hash map.
Below is the implementation of the data structure.

"""

'''
Python program to design a DS that
supports following operations
in Theta(n) time:
a) Insert
b) Delete
c) Search
d) getRandom
'''

# Class to represent the required
# data structure




import random
class MyDS:

    # Constructor (creates a list and a hash)
    def __init__(self):

        # A resizable array
        self.arr = []

        # A hash where keys are lists elements
        # and values are indexes of the list
        self.hashd = {}

    # A Theta(1) function to add an element
    # to MyDS data structure
    def add(self, x):

        # If element is already present,
        # then nothing has to be done
        if x in self.hashd:
            return

        # Else put element at
        # the end of the list
        s = len(self.arr)
        self.arr.append(x)

        # Also put it into hash
        self.hashd[x] = s

    # A Theta(1) function to remove an element
    # from MyDS data structure
    def remove(self, x):

        # Check if element is present
        index = self.hashd.get(x, None)
        if index == None:
            return

        # If present, then remove
        # element from hash
        del self.hashd[x]

        # Swap element with last element
        # so that removal from the list
        # can be done in O(1) time
        size = len(self.arr)
        last = self.arr[size - 1]
        self.arr[index], \
            self.arr[size - 1] = self.arr[size - 1], \
            self.arr[index]

        # Remove last element (This is O(1))
        del self.arr[-1]

        # Update hash table for
        # new index of last element
        self.hashd[last] = index

    # Returns a random element from MyDS
    def getRandom(self):

        # Find a random index from 0 to size - 1
        index = random.randrange(0, len(self.arr))

        # Return element at randomly picked index
        return self.arr[index]

    # Returns index of element
    # if element is present,
    # otherwise none
    def search(self, x):
        return self.hashd.get(x, None)


# Driver Code
if __name__ == "__main__":
    ds = MyDS()
    ds.add(10)
    ds.add(20)
    ds.add(30)
    ds.add(40)
    print(ds.search(30))
    ds.remove(20)
    ds.add(50)
    print(ds.search(50))
    print(ds.getRandom())

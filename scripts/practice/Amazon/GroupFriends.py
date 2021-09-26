"""

Group Friends

Design a solution which can preform the following operations

Given two IDs, associate those IDs as friends, and any existing friends of those IDs also become friends (if 1 and 2 are friends, and 2 and 3 are friends, then 1 and 3 are also friends).
Given two IDs, return true if they are friends.
Return the size of the largest group of friends.

Example:

1. (1, 2) -> {1, 2}
2. (3, 4) -> {1, 2} {3, 4}
3. (2, 3) -> {1, 2, 3, 4}

"""

from collections import *


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = val
        self.rank = 0


class Solution:

    def __init__(self):
        self.collection = dict()

    def addfriend(self, f1, f2):

        fNode1 = None
        fNode2 = None
        if f1 not in self.collection:
            fNode1 = Node(f1)
            self.collection[f1] = fNode1
        else:
            fNode1 = self.collection[f1]

        if f2 not in self.collection:
            fNode2 = Node(f2)
            self.collection[f2] = fNode2
        else:
            fNode2 = self.collection[f2]

        if fNode1.rank == fNode2.rank:
            fNode1.rank += 1
            fNode2.parent = fNode1.val
        elif fNode1.rank > fNode2.rank:
            fNode2.parent = fNode1.val
        else:
            fNode1.parent = fNode2.val

    def find(self, f):
        if f not in self.collection:
            return None

        while self.collection[f].parent != f:
            return self.find(self.collection[f].parent)
        return self.collection[f].parent

    def findFriendShip(self, f1, f2):
        if f1 not in self.collection or f2 not in self.collection:
            return False

        fNode1 = self.find(f1)
        fNode2 = self.find(f2)

        return self.collection[fNode1].parent == self.collection[fNode2].parent


s = Solution()
s.addfriend(1, 2)
s.addfriend(2, 3)
s.addfriend(3, 4)
s.addfriend(5, 6)
assert s.findFriendShip(1, 4) == True
assert s.findFriendShip(2, 3) == True
assert s.findFriendShip(1, 5) == False


#  Union find
"""

- self.nums is a dictionary introduced to map given ID to index of the list 
self.friend since the ID is not guaranteed to be in an ascending order starting from 1.
- self.friend is a list with its index (>0) representing number of corresponding 
objects and value as its ''root''. For example,self.friend = [0, 2, -3, 2], 
the negative sign in -3 (index 2) means that No.2 is the root (of both No. 1 and No. 3) 
and its absolute value 3 means that there're in total 3 friends in this group. 
And 2 at index 1 means that the root for this index is at index 2.
- self.index is used to increment the index in the list self.friend as more IDs are added.

"""


class Solution:

    def __init__(self):
        self.friend = [0]
        self.nums = {}
        self.index = 1

    def friendGroup(self, id):
        '''associate two IDs as friends'''
        if id[0] not in self.nums and id[1] not in self.nums:
            self.friend.extend([-1, -1])
            self.nums[id[0]] = self.index
            self.nums[id[1]] = self.index+1
            self.index += 2
        elif id[0] not in self.nums:
            self.friend.extend([-1])
            self.nums[id[0]] = self.index
            self.index += 1
        elif id[1] not in self.nums:
            self.friend.extend([-1])
            self.nums[id[1]] = self.index
            self.index += 1

        num0, num1 = self.nums[id[0]], self.nums[id[1]]
        self.union(num0, num1)
        return -min(self.friend)
        # return the size of the largest group of friends.

    def isfriend(self, id):
        '''check if two IDs are friends already'''
        if id[0] not in self.nums or id[1] not in self.nums:
            return False
        else:
            return self.find(self.nums[id[0]]) == self.find(self.nums[id[1]])

    def union(self, a, b):
        '''make unions'''
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.friend[root_a] > self.friend[root_b]:
                root_a, root_b = root_b, root_a
            self.friend[root_a] += self.friend[root_b]
            self.friend[root_b] = root_a

    def find(self, a):
        '''find the root'''
        while self.friend[a] > 0:
            a = self.friend[a]
        return a


# Another way with new methods


class Friends:
    def __init__(self):
        self.friends = defaultdict(list)

    def Group(self, friends):
        for f1 in friends:
            for f2 in friends:
                if f1 != f2:
                    self.makeFriends(f1, f2)

    def makeFriends(self, f1, f2):
        self.friends[f2].append(f1)
        self.friends[f1].append(f2)

        return self.printGroups()

    def areFriends(self, f1, f2):
        visited = {}

        def dfs(f):
            if visited.get(f):
                return False
            visited[f] = True
            if f == f2:
                return True

            for fof in self.friends[f]:
                if dfs(fof):
                    return True

            return False

        return print(dfs(f1))

    def printGroups(self):
        groups = []
        visited = {}

        def dfs(n, container):
            if visited.get(n):
                return
            visited[n] = True
            container.append(n)
            for i in self.friends[n]:
                dfs(i, container)

            return
        for p in self.friends.keys():
            group = []
            if visited.get(p) is None:
                dfs(p, group)
            if(len(group)):
                groups.append(group)

        return print(groups)


testObj = Friends()
testObj.makeFriends(1, 2)
testObj.areFriends(1, 2)
testObj.areFriends(3, 4)
testObj.makeFriends(3, 4)
testObj.areFriends(1, 2)
testObj.areFriends(3, 4)
testObj.areFriends(2, 3)
testObj.makeFriends(2, 3)
testObj.areFriends(1, 4)

'''
[[2, 1]]         
True             
False            
[[2, 1], [3, 4]] 
True             
True             
False            
[[2, 1, 3, 4]]   
True             
'''

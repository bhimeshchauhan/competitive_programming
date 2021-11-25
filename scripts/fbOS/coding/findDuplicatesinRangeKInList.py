# -*- coding: utf-8 -*-
"""

Find duplicates within a range k in an array

Given an array and a positive number k, check whether the array contains any duplicate elements within the range k. If k is more than the array’s size, the solution should check for duplicates in the complete array.

For example,

Input:

nums[] = { 5, 6, 8, 2, 4, 6, 9 }
k = 4

Output: Duplicates found

(element 6 repeats at distance 4 which is <= k)

Input:

nums[] = { 5, 6, 8, 2, 4, 6, 9 }
k = 2

Output: No duplicates were found

(element 6 repeats at distance 4 which is > k) 

Input:

nums[] = { 1, 2, 3, 2, 1 }
k = 7

Output: Duplicates found

(element 1 and 2 repeats at distance 4 and 2, respectively which are both <= k)
Practice this problem

A naive solution would be to consider every subarray of size k and check for duplicates in it. The time complexity of this solution is O(n.k2) since there can be n subarrays of size k, and each subarray might take O(k2) time for checking duplicates.

The problem can be efficiently solved using hashing in O(n) time and O(n) extra space. The idea is to traverse the array and store each element and its index in a map, i.e., (element, index) as (key, value) pairs in a map. If any element is already found present on the map, check if that element repeats within the range of k using its previous occurrence information from the map.

"""


def hasDuplicate(nums, k):

    # stores (element, index) pairs as (key, value) pairs
    d = {}

    # traverse the list
    for i, e in enumerate(nums):

        # if the current element already exists in the dictionary
        if e in d:

            # return true if the current element repeats within range of `k`
            if i - d.get(e) <= k:
                return True

        # store elements along with their indices
        d[e] = i

    # we reach here when no element repeats within range `k`
    return False


if __name__ == '__main__':

    nums = [5, 6, 8, 2, 4, 6, 9]
    k = 4

    if hasDuplicate(nums, k):
        print('Duplicates found')
    else:
        print('No duplicates were found')

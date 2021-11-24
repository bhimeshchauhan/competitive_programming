# -*- coding: utf-8 -*-
"""

Sort a k-sorted array

A simple solution would be to use an efficient sorting algorithm to sort the whole array again. The worst-case time complexity of this approach will be O(n.log(n)), where n is the size of the input. This method also does not use the fact that the array is k–sorted. We can also use the insertion sort algorithm to correct the order in just O(n.k) time. Insertion sort performs really well for small values of k, but it’s not recommended for a large value of k (we can use it for k < 12).

We can solve this problem in O(n.log(k)) using a min-heap. The idea is to construct a min-heap of size k+1 and insert the first k+1 elements into the heap. Then remove minimum from the heap and insert the next element from the array into the heap and continue the process till both array and heap are exhausted. Each pop operation from the heap should insert the corresponding top element in its correct position into the array.

=====

Got asked this question for Facebook onsite (London) round today. Have never seen this before. Let me know if there is already a question on LC for this.

Description : You are given an array and a integer k.
Let's define the target position of every element as the index at which it would appear if this element was sorted.
For example, if the array is [1, 2, 3, 4, 5] then the target position for 1 is 0, for 2 is 1 and so on.

Now, every element in the array is present at either its target position or k indexes away from its target position.

For instance, if the target position of an element is index 5, and k = 2, then this element may be present anywhere between indexes [3, 7] included.

The task is to sort the array.

Example input : [1, 4, 5, 2, 3, 8, 7, 6], k = 2
Expected output : [1, 2, 3, 4, 5, 6, 7, 8]

I could only come up with a TC : O(n logk), SC : O(k) solution involving a heap and sliding window of size k.

Is there a O(n) solution?
My interviewer was a brick wall throughout the interview, I have no clue what they wanted.

"""

import heapq
from heapq import heappop, heappush


# Function to sort a k–sorted array
def sort_k_sorted_arr(nums, k):

    # build a min-heap from the first `k+1` elements in the list
    pq = nums[0:k+1]
    heapq.heapify(pq)

    # do for remaining elements in the list
    index = 0
    for i in range(k+1, len(nums)):

        # pop the top element from the min-heap and assign them to the
        # next available list index
        nums[index] = heappop(pq)
        index = index + 1

        # push the next list element into min-heap
        heappush(pq, nums[i])

    # pop all remaining elements from the min-heap and assign them to the
    # next available list index
    while pq:
        nums[index] = heappop(pq)
        index = index + 1


if __name__ == '__main__':

    nums = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2

    sort_k_sorted_arr(nums, k)
    print(nums)

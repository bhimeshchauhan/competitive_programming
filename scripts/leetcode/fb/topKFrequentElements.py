"""

Given an integer array nums and an integer k, return the 
k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


"""

# Two solutions

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = {}
        frq = {}
        for i in range(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z, v in hs.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        print(hs, frq)

        arr = []

        for x in range(len(nums), 0, -1):
            print('x', x)
            if x in frq:
                for i in frq[x]:
                    arr.append(i)

        return [arr[x] for x in range(0, k)]

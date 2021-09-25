"""

Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: 
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length

"""
from collections import OrderedDict


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ans = l = 0
        # Last seen index of an integer
        od = OrderedDict()
        for i, n in enumerate(A):
            od[n] = i
            od.move_to_end(n)
            while len(od) > K:
                l = od.popitem(last=False)[1] + 1
            if len(od) == K:
                # The smallest index in od - left bound + 1
                ans += next(iter(od.items()))[1] - l + 1
        return ans

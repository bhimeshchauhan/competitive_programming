"""

Partition Equal Subset Sum

https://leetcode.com/problems/partition-equal-subset-sum/


Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s//2
        memo = {}

        def helper(nums, idx, target):
            if target == 0:
                return True
            if target < 0 or idx >= n:
                return False
            if (idx, target) not in memo:
                memo[(idx, target)] = helper(nums, idx+1, target -
                                             nums[idx]) or helper(nums, idx+1, target)
            return memo[(idx, target)]
        return helper(nums, 0, target)

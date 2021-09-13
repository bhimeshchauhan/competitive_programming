"""

Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ref = {0:1}
        add = 0
        count = 0
        for num in nums:
            add += num
            if add-k in ref:
                count += ref[add-k]
            ref[add]=ref.get(add, 0) + 1
        
        return count
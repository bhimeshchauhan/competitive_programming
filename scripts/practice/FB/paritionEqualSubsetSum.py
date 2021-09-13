"""

Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

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

from copy import deepcopy
from functools import lru_cache
class Solution:
    def canPartition(self, nums):

        @lru_cache(maxsize=None)
        def dp(subsetSum, n, nums):
            if subsetSum == 0:
                return True

            if subsetSum < 0 or n == 0:
                return False
            
            return dp(subsetSum-nums[n-1], n-1, nums) or dp(subsetSum, n-1, nums)

        if sum(nums) % 2 != 0:
            return False
        return dp(subsetSum=sum(nums)//2, n=len(nums)-1, nums=tuple(nums))


if __name__ == "__main__":
    nums = [1,5,11,5]
    print(Solution().canPartition(nums))

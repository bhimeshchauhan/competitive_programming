"""
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

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

[2, 2, 1, 1]
 ^  ^     ^
"""

class Solution:
    def canPartition(self, nums):
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        print(dp)
        for curr in nums:
            print('curr', curr)
            for j in range(subset_sum, curr - 1, -1):
                print('j ', j)
                print('dp[j] or dp[j - curr] ', dp[j] or dp[j - curr])
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]        
        
if __name__ == "__main__":
    nums = [2,2,1,1]
    print(Solution().canPartition(nums))
        
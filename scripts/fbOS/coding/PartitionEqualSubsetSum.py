"""

Partition Equal Subset Sum

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

"""

The idea is to decide whether to include a number in sum or not and then check if equal to the sum.

"""




from functools import lru_cache
class Solution:
    def canPartition(self, nums):
        @lru_cache(maxsize=None)
        def dfs(nums, n, subset_sum):
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                      or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        # we need to find combination that ends up in this sum
        subset_sum = total_sum // 2
        n = len(nums)
        # we pass in the subset_sum here and reduce it to 0 if we come across 0 then we have the subset
        return dfs(tuple(nums), n - 1, subset_sum)


if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartition([1, 5, 11, 5]))
    print(sol.canPartition([1, 2, 3, 5]))
    print(sol.canPartition([14,9,8,4,3,2]))
    print(sol.canPartition([6, 7, 4, 3]))

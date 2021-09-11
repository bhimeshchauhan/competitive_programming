"""

Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each
integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them
to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

"""

"""

# Intuition

target = 3

[1,1,1,1,1]
         ^
"""




from copy import deepcopy
class Solution:
    def findTargetSumWays(self, nums, target):

        def targetSum(nums, target, idx=len(nums)-1, curr_sum=0):
            # Base Cases
            if idx < 0 and curr_sum == target:
                return 1
            if idx < 0:
                return 0

            # Decisions
            positive = targetSum(nums, target, idx-1, curr_sum + nums[idx])
            negative = targetSum(nums, target, idx-1, curr_sum + -nums[idx])

            return positive + negative

        return targetSum(nums, target)


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(Solution().findTargetSumWays(nums, target))

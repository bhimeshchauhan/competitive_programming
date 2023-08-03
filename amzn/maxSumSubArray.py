"""_summary_

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the 
divide and conquer approach, which is more subtle.

"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        total_max = nums[0]
        
        for num in nums:
            # here is the trick, we need max of the current number we are looking at or
            # we will pick the sum of current_max and the number we are looking at.
            current_max = max(num, current_max+num)
            total_max = max(total_max, current_max)
        return total_max
    

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
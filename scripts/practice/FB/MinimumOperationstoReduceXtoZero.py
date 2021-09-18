"""

Minimum Operations to Reduce X to Zero

You are given an integer array nums and an integer x. In one operation, you can either remove the 
leftmost or the rightmost element from the array nums and subtract its value from x. Note that 
this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements 
(5 operations in total) to reduce x to zero. 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109

"""
"""

Idea is to do using continous subarray with max length size which return continous subarray length. 
The elements that are not included in the subarray (exterior to it) is the ans. 
So, in this case len(nums) - maxLen of continous subarray.
Now x is actually sum of exterior, to do continous subarray we need total sum - x (exclude x sum)

"""
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        maxLen = total = windowStart = 0
        targetSum = sum(nums)
        
        # edge cases
        if targetSum < x: return -1
        if targetSum == x: return len(nums)
        
        # opposite of sliding window but still do sliding window
        # so instead of find continous subarray,
        # we need to find outer points that is not included in continous subarray
        k = targetSum - x # this is for continous subarray
        
        for windowEnd in range(len(nums)):
            total += nums[windowEnd]
            
            while total > k:
                total -= nums[windowStart]
                windowStart += 1
            
            if total == k:
                maxLen = max(maxLen, windowEnd - windowStart + 1)
    
        
        return len(nums) - maxLen if maxLen != 0 else -1
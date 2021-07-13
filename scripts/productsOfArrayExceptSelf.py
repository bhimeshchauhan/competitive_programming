"""
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count 
as extra space for space complexity analysis.)
"""
import copy
class Solution:
    def productExceptSelf(self, nums):
        # product = 1
        # result = copy.deepcopy(nums)
        # for num in nums:
        #     if num != 0:
        #         product *= num
        
        # for idx in range(len(nums)):
        #     if 0 in nums[:idx] or 0 in nums[idx+1:]:
        #         result[idx] = 0
        #     elif nums[idx] != 0:
        #         result[idx] = product // nums[idx]
        #     else:
        #         result[idx] = product
        # return result

        length = len(nums)
        answer = [0]*length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        multiplier = 1;
        for i in reversed(range(length)):
            answer[i] = answer[i] * multiplier
            multiplier *= nums[i]
        return answer

        

if __name__ == "__main__":
    nums = [1, 2]
    print(Solution().productExceptSelf(nums))
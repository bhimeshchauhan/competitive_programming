"""

Product of Array Except Self

Given an integer array nums, return an 
array answer such that answer[i] is equal 
to the product of all the elements 
of nums except nums[i].

The product of any prefix or suffix of nums 
is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs 
in O(n) time and without using the 
division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30

The product of any prefix or suffix of nums 
is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in 
O(1) extra space complexity? 
(The output array does not count as 
extra space for space complexity analysis.)

"""

"""
01 02 03 04
24 12 08 06

01 01 02 06
24 12 04 01

24 12 08 06
"""


class Solution:
    def productExceptSelf(self, nums):
        leftProduct = [1]
        rightProduct = [1]
        reversedNums = list(reversed(nums))

        for num in nums[:-1]:
            leftProduct.append(leftProduct[-1]*num)
        for num in reversedNums[:-1]:
            rightProduct.append(rightProduct[-1]*num)
        rightProduct = list(reversed(rightProduct))

        ans = []
        for idx in range(len(leftProduct)):
            ans.append(leftProduct[idx]*rightProduct[idx])
        return ans


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))

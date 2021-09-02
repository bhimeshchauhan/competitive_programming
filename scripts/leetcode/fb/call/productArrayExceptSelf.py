"""

Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

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

"""


class Solution:
    def productExceptSelf(self, nums):
        leftProduct = []
        rightProduct = []
        for idx in range(len(nums)-1):
            if idx == 0:
                leftProduct.append(1)
            leftProduct.append(leftProduct[-1] * nums[idx])
        
        for idx in range(len(nums)-1, 0, -1):
            if idx == len(nums)-1:
                rightProduct.append(1)
            rightProduct.append(rightProduct[-1] * nums[idx])
        
        res = []
        rightProduct = list(reversed(rightProduct))
        for idx in range(len(leftProduct)):
            product = leftProduct[idx] * rightProduct[idx]
            res.append(product)
            
        return res
    
    def productExceptSelf2(self, nums):
        leftProduct = []
        rightProduct = []
        for idx in range(len(nums)-1):
            if idx == 0:
                leftProduct.append(1)
            leftProduct.append(leftProduct[-1] * nums[idx])

        multiplier = 1
        for idx in range(len(nums)-1, -1, -1):
            leftProduct[idx] *= multiplier
            multiplier *= nums[idx]
            
        return leftProduct
    


if __name__ == "__main__":
    nums = [4, 5, 1, 8, 2, 10, 6]
    print(Solution().productExceptSelf(nums))
    print(Solution().productExceptSelf2(nums))

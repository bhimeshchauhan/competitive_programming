"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use
the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109


Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store a dictionary with key as the difference between the number
        # you are looking at and the target and value as the index of the number
        # you are currently looking at.
        tally = {}
        
        for index, num in enumerate(nums):
            # find the difference
            diff = target - num
            # if the item is in the dictionary defined above then
            if diff in tally:
                # return the index of the difference and the index of the number
                # you are currently looking at
                return [tally[diff], index]
            # if the item is not int he dictionary then add it
            tally[num] = index
    
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums = nums, target = target))
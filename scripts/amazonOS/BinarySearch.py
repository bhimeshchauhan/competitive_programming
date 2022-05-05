"""

Binary Search

https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self._binary_search(nums, target, 0, len(nums))

    def _binary_search(self, nums, target, low, high):

        # You have reached a subspace of size 0
        if low == high:
            return -1

        # Remember to add low to the pointer, since you are not changing nums
        pointer = low + int((high-low)/2)

        # Search for target integer, and adjust search space in sorted array if target is not found
        if nums[pointer] == target:
            return pointer
        elif nums[pointer] > target:
            return self._binary_search(nums, target, low, pointer)
        else:
            return self._binary_search(nums, target, pointer+1, high)


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums, target))

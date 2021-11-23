"""

Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and 
ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109


"""

# Calculation based approach


class Solution:
    def searchRange(self, nums, target):
        res = [-1, -1]

        for idx, item in enumerate(nums):
            if item == target:
                res[0] = idx
                break

        for idx, item in enumerate(reversed(nums)):
            if item == target:
                res[-1] = len(nums)-idx-1
                break

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sol.searchRange(nums, target))

# Binary Search


class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

        def searchLow(nums, target):
            head, tail = 0, len(nums) - 1
            while head <= tail:
                mid = (head + tail)//2
                if nums[mid] >= target:
                    tail = mid - 1
                else:
                    head = mid + 1
            return head

        def searchHigh(nums, target):
            head, tail = 0, len(nums) - 1
            while head <= tail:
                mid = (head + tail)//2
                if nums[mid] > target:
                    tail = mid - 1
                else:
                    head = mid + 1
            return tail

        start = searchLow(nums, target)
        end = searchHigh(nums, target)
        if 0 <= start < len(nums) and start <= end and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sol.searchRange(nums, target))

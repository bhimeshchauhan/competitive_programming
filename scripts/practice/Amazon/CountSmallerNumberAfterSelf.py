"""

Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller 
elements to the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:

Input: nums = [-1]
Output: [0]

Example 3:

Input: nums = [-1,-1]
Output: [0,0]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

"""


class Solution:
    def binarySearch(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        res = -1
        while lo <= hi:
            mid = (lo+hi) // 2
            #print(lo, hi, mid)
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                res = mid
                hi = mid - 1
        return res

    def countSmaller(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        res = []

        for i in range(len(nums)):
            print(nums_sorted, i, nums[i])
            idx = self.binarySearch(nums_sorted, nums[i])
            print(idx)
            res.append(idx)
            print(res)
            nums_sorted.pop(idx)

        return res

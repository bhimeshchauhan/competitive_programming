"""

Maximum Length of Subarray With Positive Product

https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

"""


from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        n = len(nums)
        pos = [0] * n  # (1)
        neg = [0] * n  # (2)

        pos[0] = 1 if nums[0] > 0 else 0
        neg[0] = 1 if nums[0] < 0 else 0

        for i in range(1, n):
            if nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] else 0
                neg[i] = 1 + pos[i - 1] if pos[i - 1] else 1
            elif nums[i] > 0:
                pos[i] = 1 + pos[i - 1] if pos[i - 1] else 1
                neg[i] = 1 + neg[i - 1] if neg[i - 1] else 0

        return max(pos)

    # The idea is to keep track of the maximum length of subarray with negative product and maximum length of subarray with positive product, because depending on the sign of each number we encounter, we want to use each length to inform the other.
    # (1) pos[i] = maximum subarray length with positive product including nums[i] so far
    # (2) neg[i] = maximum subarray length with negative product including nums[i] so far
    # Here are the different possible cases:
    #   - If the number is negative:

    #       - If there is a non-empty subarray with negative product to the immediate left of this number:
    #           - Add this number to the subarray with positive product, since negative times negative equals positive.
    #       - Otherwise:
    #           - No subarray with positive product at this point.

    #       - If there is a non-empty subarray with positive product to the immediate left of this number:
    #           - Add this number to subarray with negative product, since positive times negative equals negative.
    #       - Otherwise:
    #           - Begin a new subarray with negative product, since a single negative value has a negative product.

    #   - If the number is positive:

    #       - If there is a non-empty subarray with positive product to the immediate left of this number:
    #           - Add this number to the subarray with positive product, since positive times positive equals positive.
    #       - Otherwise:
    #           - Begin a new subarray with positive product, since a single positive value has a positive product.

    #       - If there is a non-empty subarray with negative product to the immediate left of this number:
    #           - Add this number to subarray with negative product, since negative times positive equals negative.
    #       - Otherwise:
    #           - No array with negative product at this point.

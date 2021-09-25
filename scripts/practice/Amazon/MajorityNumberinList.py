"""

Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1

Follow-up: Could you solve the problem in linear time and in O(1) space?

"""

# Brute Force

"""
Time complexity : O(n^2)
Space complexity : O(1)
"""




import collections
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

# Hashmap


"""
Time complexity : O(n)
Space complexity : O(n)
"""


class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# Sorting


"""
Time complexity : O(nlogn)
Space complexity : O(1) or (O(n))
"""


class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# Boyer-Moore Voting Algorithm


"""
Time complexity : O(n)
Space complexity : O(1)
"""


class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

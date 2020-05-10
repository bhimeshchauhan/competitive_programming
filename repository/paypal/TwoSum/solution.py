"""
Intuition

The idea is to maintain a dictionary awith the number as key and index as value
and then retrieve the see if any difference exists and return the indices.

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tally = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in tally:
                return [tally[difference], i]
            else:
                tally[nums[i]] = i

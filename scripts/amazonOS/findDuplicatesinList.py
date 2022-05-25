from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        save = []

        sorts = sorted(nums)        # sort nums

        # iterate through nums, if sorts[i] = sorts[i+1], append sorts[i]
        for i in range(len(nums)-1):
            if sorts[i] == sorts[i+1]:
                save.append(sorts[i])

        return save

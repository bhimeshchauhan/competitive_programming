"""

subsets

https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.


"""

# DFS


from collections import deque
import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(subset=[], index=0):

            if index == len(nums):
                result.append(subset)
                return

            dfs(subset + [nums[index]], index + 1)
            dfs(subset, index + 1)

        dfs()
        return result


# BFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        queue = deque([])

        for i in range(len(nums)):
            queue.append(([nums[i]], i))

        return self.bfs(queue, nums)

    def bfs(self, queue, nums):
        result = [[]]
        while queue:
            curPath, idx = queue.popleft()

            result.append(curPath)

            for i in range(idx+1, len(nums)):
                queue.append((curPath + [nums[i]], i))

        return result


# itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(nums)+1):
            for k in itertools.combinations(nums, i):
                result.append(k)

        return result

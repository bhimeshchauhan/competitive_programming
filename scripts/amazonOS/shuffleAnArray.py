"""init saves the list and the length of the list
reset simply returns the list O(1)
shuffle starts with a list of possible positions to extract from nums and randomly selects a position one by one, while removing the extracted position from positions. Removing from positions happens in O(1) time because we place the last element of positions in the index to remove, and then remove the last element from positions. (Total time complexity O(n) because we extract from nums and add to result n times)
"""


from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        result = []
        positions = list(range(self.length))
        l = self.length
        while l > 0:
            rand = 0
            if l > 1:
                rand = random.choice(range(l))

            result.append(self.nums[positions[rand]])

            positions[rand] = positions[-1]
            del positions[l-1]

            l -= 1
        return result

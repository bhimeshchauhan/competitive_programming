"""

Is Rotated Sorted List

Implement an algorithm that detects a rotated, sorted list.

"""

from typing import List


def isRotatedSortedList(nums: List[int]):
    foundSeam = False
    prev = None
    for i in nums:
        if prev and i < prev:
            if foundSeam:
                return False
            foundSeam = True
        prev = i
    return True


if __name__ == "__main__":
    nums = [4, 6, 7, 8, 1, 3]
    print(isRotatedSortedList(nums))

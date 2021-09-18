"""

Find K Closest Elements
 
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]: 
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]

        left = 0
        right = len(arr) - k # max start point
        while left < right:
            mid = left + (right - left) // 2

            # mid + k is closer to x, discard mid by assigning left = mid + 1
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1

            # mid is equal or closer to x than mid + k, remains mid as candidate
            else:
                right = mid

        # left == right, which makes both left and left + k have same diff with x
        return arr[left : left + k]

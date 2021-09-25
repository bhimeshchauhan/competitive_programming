"""

Trapping Rain Water

Given n non-negative integers representing an elevation map where the 
width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

"""

Complextiy

Time Complexity: O(n^2)
Space Complexity: O(1)

"""


def trap(self, bars):
    # base case if no bars are present or are less than 3
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    # start pointers from both ends
    left, right = 0, len(bars) - 1
    # current left and right max as the ones initiated
    l_max, r_max = bars[left], bars[right]
    # While left and right pointers have not crossed each other
    while left < right:
        # Get left max and right max
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        # if left max is less than equal to right max
        if l_max <= r_max:
            # volume is on left side of the bars
            volume += l_max - bars[left]
            left += 1
        # if left max is greater than right max
        else:
            # volume is on the right side of the bars
            volume += r_max - bars[right]
            right -= 1
    return volume


"""

Complexity analysis

Time complexity: O(n). Single iteration of O(n).
Space complexity: O(1) extra space. Only constant space required 
for left, right, left_max and right_max.

"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areas = 0
        max_l = max_r = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    areas += max_l - height[l]
                l += 1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    areas += max_r - height[r]
                r -= 1
        return areas

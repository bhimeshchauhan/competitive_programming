"""

Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108

"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        
        i = 1
        res = [c for c in str(num)]
        n = len(res)
        
        # Find the "inflection point" (i.e. the first digit that is greater than
        # its previous digit).
        while i < n:
            if res[i] > res[i - 1]:
                break
            i += 1
        
        # If we have reached the end of res, that means the number is
        # strictly decreasing. This means we should not swap any digits
        # because the number is already the largest it can be.
        if i == n:
            return num
        
        bigToSwapIdx = j = i
        
        # Find the rightmost largest number after the inflection (inclusive).
        while j < n:
            if res[j] >= res[bigToSwapIdx]:
                bigToSwapIdx = j
            j += 1
            
        smallToSwapIdx = 0
        
        # Find the first number that is smaller than res[bigToSwapIdx]
        # that resides in the leftside of the inflection point (exclusive).
        while smallToSwapIdx < i:
            if res[smallToSwapIdx] < res[bigToSwapIdx]:
                break
            smallToSwapIdx += 1
            
        # Swap
        res[smallToSwapIdx], res[bigToSwapIdx] = res[bigToSwapIdx], res[smallToSwapIdx]
        
        return int("".join(res))
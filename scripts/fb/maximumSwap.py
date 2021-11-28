"""
Maximum Swap digits in a number to gt Max number

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
    def maximumSwap(self, num):
        maxNum = num
        idx, jdx = 0, 0
        while idx < len(str(num)):
            for jdx in range(len(str(num))):
                strNum = list(str(num))
                if(idx != jdx and strNum[jdx]>strNum[idx]):
                    strNum[idx],strNum[jdx]=strNum[jdx],strNum[idx]
                    maxNum = max(maxNum, int(''.join(strNum)))
            idx += 1
        return maxNum
    
if __name__ == "__main__":
    num = 2736
    print(Solution().maximumSwap(num))
"""

Number of Ways to Split a String

Given a binary string s (a string consisting only of '0's and '1's), 
we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).

Return the number of ways s can be split such that the number of 
characters '1' is the same in s1, s2, and s3.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"

Example 2:

Input: s = "1001"
Output: 0

Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"

Example 4:

Input: s = "100100010100110"
Output: 12

Constraints:

3 <= s.length <= 10^5
s[i] is '0' or '1'.

"""

class Solution:
    def numWays(self, s: str) -> int:
        ones = 0

        # Count number of Ones
        for char in s:
            if char == "1":
                ones += 1

        # Can't be grouped equally if the ones are not divisible by 3
        if ones > 0 and ones % 3 != 0:
            return 0

        # Ways of selecting two dividers from n - 1 dividers 
        if ones == 0:
            n = len(s)
			# n = {3: 1, 4: 3, 5: 6, 6: 10, 7: 15 ... }
            return (((n - 1) * (n - 2)) // 2) % ((10 ** 9) + 7)

        # Number of ones in each group
        ones_interval = ones // 3

        # Number of zeroes which lie on the borders
        left, right = 0, 0

        # Iterator
        i = 0
        temp = 0

        # Finding the zeroes on the left and right border
        while i < len(s):
            temp += int(s[i]) & 1
            if temp == ones_interval:
                if s[i] == '0':
                    left += 1
            if temp == 2 * ones_interval:
                if s[i] == '0':
                    right += 1
            i += 1
        
        # The result is the product of number of (left + 1) and (right + 1)
        # Because let's assume it as we only want to fill up the middle group
        # The solution would be if we have zero then there might be a zero in the middle
        # Or there might not be the zero, so this might case is added and then
		# the events are independent so product of both the events
        return ((left + 1) * (right + 1)) % ((10 ** 9) + 7)
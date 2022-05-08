"""

Longest Palindrome

https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1

Example 3:

Input: s = "bb"
Output: 2

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.

"""


class Solution:
    def longestPalindrome(self, s):
        from collections import Counter

        freq = Counter(s)

        odd = False
        res = 0

        for k, v in freq.items():
            if v % 2 == 0:
                res += v
            else:
                res += v-1
                odd = True

        if odd:
            res += 1

        return res


if __name__ == "__maine__":
    s = "abccccdd"
    print(s)
    print(Solution().longestPalindrome(s))

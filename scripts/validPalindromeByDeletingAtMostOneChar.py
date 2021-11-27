"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.

"""


class Solution:
    def validPalindrome(self, s):
        def verify(s, left, right, deleted):
            while left < right:
                if s[left] != s[right]:
                    # For generalized approach make deleted a counter
                    if deleted:
                        return False
                    else:
                        return verify(s, left+1, right, True) or verify(s, left, right-1, True)
                else:
                    left += 1
                    right -= 1
            return True
        return verify(s, 0, len(s)-1, False)


if __name__ == "__main__":
    s = "abcdba"
    print(Solution().validPalindrome(s))

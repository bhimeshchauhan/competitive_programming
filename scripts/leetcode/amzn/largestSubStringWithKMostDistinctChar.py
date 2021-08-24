"""

Given a string s and an integer k, return the length of the longest 
substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50

"""
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start_ptr = 0
        ref = defaultdict()
        max_len = 0
        for end_ptr in range(len(s)):
            # frame_len = end_ptr-start_ptr+1
            ref[s[end_ptr]] = end_ptr
            if len(ref) == k+1:
                to_remove = min(ref.values())
                del ref[s[to_remove]]
                start_ptr = to_remove + 1
            max_len = max(max_len, end_ptr-start_ptr+1)
        return max_len

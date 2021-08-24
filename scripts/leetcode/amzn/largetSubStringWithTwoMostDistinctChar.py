"""

Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 105
s consists of English letters.

"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start_ptr = 0
        ref = defaultdict()
        max_len = 0
        for end_ptr in range(len(s)):
            # frame_len = end_ptr-start_ptr+1
            ref[s[end_ptr]] = end_ptr
            if len(ref) == 3:
                to_remove = min(ref.values())
                del ref[s[to_remove]]
                start_ptr = to_remove + 1
            max_len = max(max_len, end_ptr-start_ptr+1)
        return max_len

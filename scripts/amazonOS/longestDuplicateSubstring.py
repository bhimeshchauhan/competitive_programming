"""

Longest Duplicate Substring

https://leetcode.com/problems/longest-duplicate-substring/

Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

Example 1:

Input: s = "banana"
Output: "ana"

Example 2:

Input: s = "abcd"
Output: ""

Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.

"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ""

        # generate suffix array
        suffix_arr = [""] * len(s)
        for i in range(len(s)):
            suffix_arr[i] = s[i:]

        suffix_len = len(suffix_arr)
        suffix_arr.sort()

        # use binary search to find a double occurrence of a pattern
        def is_double_occurrence(pattern):
            l = 0
            r = suffix_len - 1
            while l < r:
                mid = (l + r) // 2
                if suffix_arr[mid].startswith(pattern):
                    # if we found an occurrence of a string, then there may be another one nearby
                    if mid - 1 >= 0 and suffix_arr[mid-1].startswith(pattern):
                        return True
                    if mid + 1 < suffix_len and suffix_arr[mid+1].startswith(pattern):
                        return True

                    # we have only single occurrence
                    return False

                if pattern > suffix_arr[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        result = ""
        window_size = 1
        for i in range(len(s)):
            while is_double_occurrence(s[i:i + window_size]):
                if i + window_size > len(s):
                    break

                result = s[i:i + window_size]
                window_size += 1

        return result


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ''
        j = 1
        for i in range(len(s)):
            longest = s[i:i+j]
            temp = s[i+1:]
            while longest in temp:
                ans = longest
                j += 1
                longest = s[i:i+j]
        return ans

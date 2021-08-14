"""
Given two strings s and p, return an array of all the start indices 
of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

"""



class Solution:
    def findAnagrams(self, s, p):
        p = ''.join(sorted(p))
        # edge cases
        if not s or not p:
            return []
        
        start_ptr, end_ptr = 0, len(p)
        anagram_indices = []
        while end_ptr <= len(s):
            print(s[start_ptr:end_ptr], start_ptr, end_ptr)
            word = s[start_ptr:end_ptr]
            print(word+''.join(reversed(word)))
            if ''.join(sorted(word)) == p:
                anagram_indices.append(start_ptr)
            if end_ptr - start_ptr >= len(p):
                start_ptr += 1
                end_ptr += 1
            else:
                end_ptr += 1
        return anagram_indices
        
if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))
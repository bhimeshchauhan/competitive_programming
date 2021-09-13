"""

Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

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

import collections
class Solution:
    def findAnagrams(self, s, p):
        myDictP = collections.Counter(p)
        myDictS = collections.Counter(s[:len(p)])
        output = []
        i = 0
        j = len(p)

        while j <= len(s):
            if myDictS == myDictP:
                output.append(i)

            myDictS[s[i]] -= 1
            if myDictS[s[i]] <= 0:
                myDictS.pop(s[i])

            if j < len(s):
                myDictS[s[j]] += 1
            j += 1
            i += 1

        return output


if __name__ == "__main__":
    s = "ababababab"
    p = "aab"
    print(Solution().findAnagrams(s, p))

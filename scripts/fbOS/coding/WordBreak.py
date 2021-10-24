"""

Word Break

Given a string s and a dictionary of strings 
wordDict, add spaces in s to construct a 
sentence where each word is a valid 
dictionary word. Return all such possible 
sentences in any order.

Note that the same word in the dictionary 
may be reused multiple times in the 
segmentation.

Example 1:

Input: s = "catsanddog", wordDict = 
["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:

Input: s = "pineapplepenapple", 
wordDict = ["apple","pen","applepen",
"pine","pineapple"]
Output: ["pine apple pen apple",
"pineapple pen apple","pine applepen apple"]
Explanation: Note that you are 
allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = 
["cats","dog","sand","and","cat"]
Output: []

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase 
English letters.
All the strings of wordDict are unique.

"""

"""
Let NN be the length of the input 
string and WW be the number of words 
in the dictionary.

Time Complexity: O(N^2 + 2^N + W)
Space Complexity: O((2^N)*N + W)

"""

from collections import defaultdict


class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)

        # @lru_cache(maxsize=None)    # alternative memoization solution
        def _wordBreak_topdown(s):
            """ return list of word lists """
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        # break the input string into lists of words list
        _wordBreak_topdown(s)

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]


if __name__ == "__main__":
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", 
                "pine", "pineapple"]
    print(Solution().wordBreak(s, wordDict))

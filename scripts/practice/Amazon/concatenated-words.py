"""

Concatenated Words


Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

Constraints:

1 <= words.length <= 10^4
0 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 10^5

"""


# Concatenated Words
# Concatenated Words is the reverse of Word Break I, so can be broken down to Word Break I.

# Sort the words according to shortest length since short ones form long words
# for each word start building our dictionary of words and check if word split is possible or not
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        preWords = set()

        # asc order of word length, since longer words are formed by shorter words
        words.sort(key=len)

        # for each short word start building preWords
        for word in words:
            if self.wordBreak(word, preWords):
                res.append(word)
            preWords.add(word)

        return res

    # Word Break I template
    def wordBreak(self, string, words):
        if not words:
            return False

        dp = [False] * (len(string) + 1)
        dp[0] = True

        for i in range(len(string)+1):
            for j in range(i):
                if dp[j] and string[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]

# Word Break II
# This is backtracking plus dynamic programming. We use dp array generated from word break I to figure out remaining string can be splitted or not, this reduces lot of backtracking calls.


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return [""]

        self.res = []
        self.wordDict = set(wordDict)
        self.dp = self.isWordBreak(s, wordDict)
        self.backtrack(s, 0, [])

        return self.res

    def backtrack(self, s, idx, path):
        # Before we backtrack, we check whether the remaining string
        # can be splitted by using the dictionary,
        # in this way we can decrease unnecessary computation greatly.
        if self.dp[idx+len(s)]:  # if word break possible then only proceed
            if not s:
                self.res.append(' '.join(path))
            else:
                for i in range(1, len(s)+1):
                    if s[:i] in self.wordDict:
                        self.backtrack(s[i:], idx+i, path + [s[:i]])

    # this is from Word Break I
    def isWordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp


# Word Break I
# Using dynamic programming to calculate if word break is possible or not

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordDict = set(wordDict)

        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

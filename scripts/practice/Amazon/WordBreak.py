"""

Word Break

Given a string s and a dictionary of strings wordDict, return true if s 
can be segmented into a space-separated sequence of one or more 
dictionary words.

Note that the same word in the dictionary may be reused multiple 
times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""

# Recursion with memoization

"""

Complexity Analysis

n is the length of the input string.

Time complexity : O(n^3) Size of recursion tree can go up to n^2.
Space complexity : O(n). The depth of recursion tree can go up to nn.

"""




from collections import deque
from collections import lru_cache
class Solution:
    def wordBreak(self, s, wordDict):
        @lru_cache
        def wordBreakMemo(s, word_dict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                    return True
            return False

        return wordBreakMemo(s, frozenset(wordDict), 0)

# Using Breadth-First-Search


"""

Complexity Analysis

n is the length of the input string.

Time complexity : O(n^3) For every starting index, the 
search can continue till the end of the given string.
Space complexity : O(n). Queue of at most nn size is needed.

"""


class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
                visited.add(start)
        return False

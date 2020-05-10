"""

Example Run

- params
    - words: ["practice", "makes", "perfect", "coding", "makes"], "practice", "coding"
    - word1: "practice"
    - word2: "coding"

run    index    current_word    last_word    current_index    ans
0      0        Null            Null         0                5
1      0        practice        Null         0                5
2      1        makes           practice     0                5
3      2        perfect         practice     0                5
4      3        coding          practice     0                5
5      4        makes           coding       3                3
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Initialize with max possible length
        ans = len(words)
        # Initialize current word and index
        current_word, current_index = None, 0
        # enumerate will also have index
        for index, word in enumerate(words):
            # If no match continue
            if word != word1 and word != word2: continue
            # If we have a current word we were looking at in last run
            # and word right now is not same
            if current_word and word != current_word:
                # result would be min of either the previous ans or difference in index from current and last run
                ans = min(ans, index - current_index)
            # store the current word and index for next run
            current_word, current_index = word, index
        # final answer
        return ans


assert Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "practice", "coding") == 3
assert Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding") == 1
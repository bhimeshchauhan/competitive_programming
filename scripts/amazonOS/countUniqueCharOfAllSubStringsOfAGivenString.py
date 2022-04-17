"""

Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s = "LEETCODE" 
then "L", "T", "C", "O", "D" are the unique characters since 
they appear only once in s, therefore countUniqueChars(s) = 5.

Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

Example 3:

Input: s = "LEETCODE"
Output: 92

Constraints:

1 <= s.length <= 105
s consists of uppercase English letters only.

"""

from collections import *


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # key: letter
        # value: list of indexes where the letter exists
        letter_index = defaultdict(list)
        for index, c in enumerate(s):
            letter_index[c].append(index)
        n = len(s)
        res = 0
        for c in letter_index:
            idxlist = letter_index[c]
            for i in range(len(idxlist)):
                """
                    For example, if the given string is "CABCBC", the second "C" is counted in the substrings "C", "BC", "ABC", "CB", "BCB", "ABCB". The number of such substrings is 6 which is same as (the number of characters between the first "C" and the second "C" + 1)*(the number of characters between the second "C" and the third "C" + 1).
                    l = (the number of characters between the first "C" and the second "C" + 1)
                    r = (the number of characters between the second "C" and the third "C" + 1)
                """
                l = idxlist[i]-(idxlist[i-1] if i != 0 else -1)
                r = (idxlist[i+1] if i+1 != len(idxlist) else n) - idxlist[i]
                res += l*r
        return res


if __name__ == "__main__":
    s = "LEETCODE"
    print(Solution().uniqueLetterString(s))

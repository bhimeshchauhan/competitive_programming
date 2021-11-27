"""

Group Shifted Strings

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]
Output: [["a"]]

Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.

"""

from collections import defaultdict


class Solution:
    def groupStrings(self, strings):
        ## RC ##
        ## APPROACH : GREEDY ##
        ## LOGIC ##
        # 1. Intuition is: there will be some relative thing in common for all those strings. Ahhh yes, difference in ascii values
        # 2. Store ascii value pairs in hashmap and group together.
        # 3. If the diff in ascii become -ve then add 26
        # Watchout : case : acz (2, 23), dfc (2, -3) ==> (2, -3+26 = 23) => can be clubbed together.

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##
        hashmap = defaultdict(list)
        for s in strings:
            key = []
            for i in range(len(s) - 1):
                # Throw in 26 so that we can normalize below
                difference = 26 + ord(s[i+1]) - ord(s[i])
                # Wrap around
                # z + 1 = a
                key.append(str(difference % 26))
            hashmap[','.join(key)].append(s)
        return list(hashmap.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
    print(s.groupStrings(["a"]))

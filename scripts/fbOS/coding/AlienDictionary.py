"""

Alien Dictionary

There is a new alien language that uses 
the English alphabet. However, the order 
among the letters is unknown to you.

You are given a list of strings words from 
the alien language's dictionary, where the 
strings in words are sorted 
lexicographically by the rules of this new 
language.

Return a string of the unique letters in 
the new alien language sorted in 
lexicographically increasing order by the 
new language's rules. If there is no solution, 
return "". If there are multiple solutions,
return any of them.

A string s is lexicographically smaller than
a string t if at the first letter where they
differ, the letter in s comes before the 
letter in t in the alien language. If the 
first min(s.length, t.length) letters are 
the same, then s is smaller if and only if
s.length < t.length.

Example 1:

Input: words = 
["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:

Input: words = ["z","x"]
Output: "zx"

Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so 
return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English 
letters.

"""

from collections import defaultdict, Counter, deque


class Solution:
    def alienOrder(self, words):
        print(list(zip(words, words[1:])))
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})
        print('adj_list', adj_list)
        print('in_degree', in_degree)

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""

        print('adj_list -> ', adj_list)
        print('in_degree -> ', in_degree)

        # Step 2: We need to repeatedly pick
        # off nodes with an indegree of 0.
        # BFS
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)


if __name__ == "__main__":
    words = ["wxqkj", "whqg", "cckgh", "cdxg", "cdxt", "cdht",
             "ktgxt", "ktgch", "ktdw", "ktdc", "jqw", "jmc", "jmg"]
    print(Solution().alienOrder(words))

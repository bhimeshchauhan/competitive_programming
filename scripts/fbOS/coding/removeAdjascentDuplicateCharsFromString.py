"""

Remove All Adjacent Duplicates in String II

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.


Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.

"""


class Solution:
    def removeDuplicatesShort(self, s, k):
        a = []
        for i in s:
            if not a:
                a.append(i)
            elif a[-1] != i:
                a.append(i)
            else:
                a.pop()
        return "".join(i for i in a)


if __name__ == "__main__":
    s = "abcd"
    k = 2
    print(Solution().removeDuplicatesShort(s, k))

    s = "deeedbbcccbdaa"
    k = 3
    print(Solution().removeDuplicatesShort(s, k))

    s = "pbbcggttciiippooaais"
    k = 2
    print(Solution().removeDuplicatesShort(s, k))


class Solution:
    def removeDuplicates(self, s, k):

        char_stack = [('bottom', 0)]

        for char in s:

            if char == char_stack[-1][0]:
                # update last character's length of adjacency
                last_char, last_adj_len = char_stack.pop()
                char_stack.append((last_char, last_adj_len+1))

            else:
                # push character with length of adjacency = 1
                char_stack.append((char, 1))

            if char_stack[-1][1] == k:
                # pop last character if it has repeated k times

                char_stack.pop()

        # generate output string
        output_str = ''.join(char*occ for char, occ in char_stack)

        return output_str


if __name__ == "__main__":
    s = "abcd"
    k = 2
    print(Solution().removeDuplicates(s, k))

    s = "deeedbbcccbdaa"
    k = 3
    print(Solution().removeDuplicates(s, k))

    s = "pbbcggttciiippooaais"
    k = 2
    print(Solution().removeDuplicates(s, k))

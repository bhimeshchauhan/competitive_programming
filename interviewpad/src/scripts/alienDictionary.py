"""In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The
order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if
the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz" Output: false Explanation: The first three
characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" >
"app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More
info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

"""


class Solution:
	def isAlienSorted(self, words: list[str], order: str) -> bool:
		print(words, order)
		refer_dict = {}
		for idx, val in enumerate(order):
			refer_dict[val] = idx
		for idx in range(len(words)):
			for jdx in range(len(words[idx])):
				if jdx >= len(words[idx + 1]):
					return False
				if words[idx][jdx] != words[idx + 1][jdx]:
					if refer_dict[words[idx][jdx]] > refer_dict[words[idx + 1][jdx]]:
						return False


if __name__ == "__main__":
	words = ["word", "world", "row"]
	order = "worldabcefghijkmnpqstuvxyz"
	print(Solution().isAlienSorted(words, order))

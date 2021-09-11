"""

Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""

from collections import deque
class Solution:
    def letterCombinations(self, digits):
        phone = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi',
                 '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        q = deque(phone[digits[0]])
        print(q)
        
        for idx in range(1, len(digits)):
            s = len(q)
            while s:
                add = q.popleft()
                for char in phone[digits[idx]]:
                    q.append(add + char)
                s -= 1
                    
        return list(q)


if __name__ == "__main__":
    digits = "239"
    print(Solution().letterCombinations(digits))

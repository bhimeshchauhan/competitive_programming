"""

Monotone Increasing Digits

An integer has monotone increasing digits if and only if 
each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is 
less than or equal to n with monotone increasing digits.

Example 1:

Input: n = 10
Output: 9

Example 2:

Input: n = 1234
Output: 1234

Example 3:

Input: n = 332
Output: 299

Constraints:

0 <= n <= 109

"""
"""
Time: O(n^2)
Space: O(1)
"""
class Solution:
    def monotoneIncreasingDigits(self, N):
        l = list(str(N))
        c = -1
        for i in range(len(l)-1): #find the first index that l[i] > l[i+1]
            if int(l[i]) > int(l[i+1]):
                c = i
                break

        if c == -1: #if N is in increasing order, return N
            return N
        else:
            while c>=1 and l[c] == l[c-1]: #if there are consecutive l[c] exits, search the first one's index
                c -= 1

            l[c+1:] = ["9"]*(len(l)-c-1) #set all the elements after c to 9
            if c>=0 and l[c] == "0": #deduct l[c] by one. if l[c] is zero, set l[c] to 9 and move backward
                while(l[c] == "0"):
                    l[c] = "9"
                    c-=1
            if c >= 0:
                l[c] = str(int(l[c])-1)
        return int("".join(l))
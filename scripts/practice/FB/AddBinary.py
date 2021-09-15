"""

ADD BINARY

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        print(a, b)
        carry = 0
        answer = []
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
                
            carry //= 2
            
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(b)<len(a):
            b='0'+b
        while len(a)<len(b):
            a='0'+a
        carry=0
        a=[int(i) for i in a]
        b=[int(i) for i in b]
        ans=''
        for i in range(len(a)-1,-1,-1):
            val=a[i]+b[i]+carry
            if val==3:
                carry=1
                ans='1'+ans
            elif val==2:
                carry=1
                ans='0'+ans
            elif val==1:
                ans='1'+ans
                carry=0
            else:
                ans='0'+ans
        return str(carry)+ans if carry else ans

"""



"""


# Bit-by-Bit Computation
"""
Time complexity: O(max(N,M)), where NN and MM are lengths of the input strings a and b.
Space complexity: O(max(N,M)) to keep the answer.
"""


class Solution:
    def addBinary(self, a, b) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
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


# Bit manipulation

"""
Time complexity : O(N+M), where NN and MM are lengths of the input strings a and b.
Space complexity : O(max(N,M)) to keep the answer.
"""


class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

"""

Count Possible Decodings of a given Digit Sequence

Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
// The possible decodings are "ABCD", "LCD", "AWD"

An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and there are no leading 0’s, no extra trailing 0’s, and no two or more consecutive 0’s.

"""

# Exponential Solution

# Recursive implementation of numDecodings


def numDecodingsHelper(s: str, n: int) -> int:
    if n == 0 or n == 1:
        return 1
    count = 0
    if s[n-1] > "0":
        count = numDecodingsHelper(s, n-1)
    if (s[n - 2] == '1'
            or (s[n - 2] == '2'
                and s[n - 1] < '7')):
        count += numDecodingsHelper(s, n - 2)
    return count


def numDecodings(s):
    if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
        return 0
    return numDecodingsHelper(s, len(s))


# Driver code
digits = "1234"
print("Count is ", numDecodings(digits))

# A Dynamic Programming based Python3
# implementation to count decodings

# A Dynamic Programming based function
# to count decodings


def countDecodingDP(digits, n):

    count = [0] * (n + 1)  # A table to store
    # results of subproblems
    count[0] = 1
    count[1] = 1

    for i in range(2, n + 1):

        count[i] = 0

        # If the last digit is not 0, then last
        # digit must add to the number of words
        if (digits[i - 1] > '0'):
            count[i] = count[i - 1]

        # If second last digit is smaller than 2
        # and last digit is smaller than 7, then
        # last two digits form a valid character
        if (digits[i - 2] == '1' or
            (digits[i - 2] == '2' and
                digits[i - 1] < '7')):
            count[i] += count[i - 2]

    return count[n]


# Driver Code
digits = "1234"
n = len(digits)
print("Count is",
      countDecodingDP(digits, n))

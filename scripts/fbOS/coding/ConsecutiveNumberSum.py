"""

Consecutive Number Sum

Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 2 + 3

Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5


Constraints:

1 <= n <= 109

"""

from math import ceil


class Solution:
    # Sum of First k Natural Numbers, O(sqrt{N})time
    # Time Complexity: O(sqrt{N})
    # Space Complexity: O(1).
    def consecutiveNumbersSumInc(self, n):
        count = 0
        upper_limit = ceil((2 * N + 0.25)**0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            # x should be integer
            if (n - k * (k + 1) // 2) % k == 0:
                count += 1
        return count

    # Sum of First k Natural Numbers, O(sqrt{N})time
    # Time Complexity: O(sqrt{N})
    # Space Complexity: O(1).
    def consecutiveNumbersSumDec(self, n):
        count = 0
        upper_limit = ceil((2 * N + 0.25)**0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            n -= k
            if n % k == 0:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.consecutiveNumbersSum(n))

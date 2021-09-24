"""

Consecutive Numbers Sum

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

# Brute Force

"""

# Let's represent N as the sum of the following series of consequetive numbers:
# N = a + (a+1) + (a+2) + ... + (a+k-1) 
# Now there are two ways to go from here:
# Approach 1 -
# Look at all possible values of 'a' and calculate 'k'
# This can be achieved using a variable length sliding window
# So we basically start calculating sum from 1, 2, 3... upto N
# if the sum equals N, add one to the result
# if the sum exceeds N, shrink the window from the left

# Time - O(N) since we iterate over all numbers from 1 to N
# Space - O(1)
# This approach will TLE, let's try to do better...

"""


class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """

        # Initialize sum to 0
        _sum = 0

        # Start window at 1
        start = 1

        # Initialize count to 0
        count = 0

        # Iterate over the range 1 to N and calculate the running sum
        for i in range(1, N+1):
            _sum += i
            # If the sum exceeds K, shrink the window
            while _sum > N:
                _sum -= start
                start += 1
            # If the sum equals N, add one to the count
            if _sum == N:
                count += 1
        return count


# Maths

"""

# Approach 2 - 
# Look at all possible values of 'k' and calculate 'a'
# From the previous series:  N = a + (a+1) + (a+2) + ... + (a+k-1) 
# For different values of k, check if a == n?
# k = 1 -> a = n
# k = 2 -> a + (a+1) == n -> a = (n-1)/2
# k = 3 -> a + (a+1) + (a+2) == n -> a = (n-3)/2
#...
# k = n -> a + (a+1) + (a+2) + (a+3) + ... +(a+n-1) == n -> a = 1
# Generalizing this,
# a + (a+1) + (a+2) + ... +(a+k-1) = n
# (k*a) + (1+2+3+...+k-1) = n
# a = (n - k*(k-1)/2)/k
# if a is in the range 1 to N and a is an integer, it is valid, add one to the count

# Time complexity:
# for a > 0, (n - k*(k-1)/2)/k > 0
# -> n - k*(k-1)/2 > 0
# -> k*(k-1)/2 < n
# -> ~ k**2 < 2*n
# -> ~ k < √2*n
# -> k ~ O(√n) FAST!

"""
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        k = 1
        count = 0
        while (N - (k*(k-1))//2) > 0:
            if (N - (k*(k-1))//2) % k == 0:
                count += 1
            k +=1
        return count

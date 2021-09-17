"""

Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.


"""

# Recursive - O(MxN) O(MxN)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # Dictionary for memoization
        memo = {}
        
        def uniqueSubsequences(i, j):
            
            M, N = len(s), len(t)
            
            # Base case
            if i == M or j == N or M - i < N - j:
                return int(j == len(t))
            
            # Check if the result is already cached
            if (i, j) in memo:
                return memo[i,j]
            
            # Always make this recursive call
            ans = uniqueSubsequences(i + 1, j)
            
            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)
            
            # Cache the answer and return
            memo[i, j] = ans
            return ans                
        
        return uniqueSubsequences(0, 0)
    
    
# Iterative Dynamic Programming - O(MxN) O(MxN)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        M, N = len(s), len(t)
        
        # Dynamic Programming table
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)] 
        
        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0
        
        # Base case initialization
        for i in range(M + 1):
            dp[i][N] = 1
        
        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
          
                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
            
        return dp[0][0]
    
    
# Space optimized Dynamic Programming - O(MxN) O(N)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        M, N = len(s), len(t)
        
        # Dynamic Programming table
        dp = [0 for j in range(N)] 
        
        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            
            # At each step we start with the last value in
            # the row which is always 1. Notice how we are
            # starting the loop from N - 1 instead of N like
            # in the previous solution.
            prev = 1
            
            for j in range(N - 1, -1, -1):
          
                # Record the current value in this cell so that
                # we can use it to calculate the value of dp[j - 1]
                old_dpj = dp[j]
        
                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[j] += prev
                
                # Update the prev variable
                prev = old_dpj    
        
        return dp[0]
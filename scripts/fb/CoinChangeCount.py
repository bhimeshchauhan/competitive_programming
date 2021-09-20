"""

Coin Change 2 - Count
 
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000

"""


# Backtracking
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {} # memoization
        def recurse(idx, rem):
            if rem == 0:
                return 1    
            if idx == len(coins):
                return 0
            if rem < 0:
                return 0
            key = '{}:{}'.format(idx,rem)
            if key in memo:
                return memo[key]
            num_ways = 0
            num_ways += recurse(idx, rem - coins[idx]) # use the current coin
            num_ways += recurse(idx + 1, rem) # Don't use the current coin
            memo[key] = num_ways
            return memo[key]
        return recurse(0, amount)
    


# DP

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
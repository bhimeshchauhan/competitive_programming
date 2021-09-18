"""


"""

# DFS

class Solution(object):
    
    def __init__(self):
        self.min_coins = float('inf')
        
    def coinChange(self, coins, amount):
        
        def helper(num_coins, need, start):
            
            divided_coin = need // coins[start]
            if num_coins + divided_coin >= self.min_coins:
                return
            if need % coins[start] == 0:
                self.min_coins = min(self.min_coins, divided_coin + num_coins)
                return
            if start == len(coins) - 1:
                return
            for num_used in range(divided_coin, -1, -1):
                new_need = need - (coins[start] * num_used)
                
                helper(num_coins + num_used, new_need, start + 1)

        coins = sorted(coins, reverse=True)
        helper(0, amount, 0)
        
        return self.min_coins if self.min_coins < float('inf') else -1


# DP

class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        
        # EDGE CASE
        if amount == 0:
            return 0
        
        # INIT DIMENSIONS
        nrows = len(coins) + 1
        ncols = amount + 1
        
        # BY DEFAULT, 2**64 DENOTES IMPOSSIBLE TO MAKE CHANGE
        dp = [[2**64 for _ in range(ncols)] for _ in range(nrows)]
        
        # BY DEFAULT, IF AMOUNT = 0, WE NEED EXACTLY 0 COINS
        for i in range(nrows):
            dp[i][0] = 0
            
        # OTHER CELLS
        for i in range(1, nrows):
            for j in range(1, ncols):
                
                # CASE 1 - WE MUST LEAVE THE COIN
                if j < coins[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                
                # CASE 2 - WE CAN TAKE OR LEAVE THE COIN
                else:
                    take = 1 + dp[i][j - coins[i - 1]]
                    leave = dp[i - 1][j]
                    dp[i][j] = min(take, leave)
        
        for row in dp:
            print(row)
            
        return -1 if dp[-1][-1] == 2**64 else dp[-1][-1]
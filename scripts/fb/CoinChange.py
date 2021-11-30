"""


"""

import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Logic, well at most index would be at index amount times. Also, it would be the same for every index
        So normally this is O(3^n), but since im guaranteeing to cache, the max possibilities of the key in cache is index*amount, so O(S*N)
        
        As for code: For each index we have 3 options: include the current coin and stay at this index
        
        include current coin and go to next index
        dont include current coin and go to next index
        For each senario, we do all three ways and then pick the min of each. 
        WE only add 1 to the part where we add a coin. 
        '''
        #I can either include the current or not include it
        cache = dict() #pair (index,sum) to amount
        def helper(index,coins,amount,cache):
            if amount == 0:
                return 0
            if index >= len(coins):
                return math.inf #If we passed all indexes and still haven't found solution, return error. IN this case it would be inf because that guarantees this path wont be the answer since we pick min of everything and inf wont ever be the min of any possible case except where the answer doesnt exist 
            if (index,amount) in cache:
                return cache[(index,amount)]
            #For each index I can:
            #   include current and go to next index
            #   include current and stay in current index
            #   not include and go to next index
            #I can also only include if
            includeNext,includeCurrent,notInclude = math.inf,math.inf,math.inf 
            #I only add it if it is possible to add the coin. This is why i set them first to be inf because if it isn't possible, these variables would return inf which we are guarnteed to not give output because of the final return statement and the fact that we are looking for the min
            if coins[index] <= amount:
                #print(amount - coins[index])
                includeNext = helper(index+1,coins,amount-coins[index],cache) +1 # we add 1 because we include it
                includeCurrent = helper(index,coins,amount-coins[index],cache) + 1
            notInclude = helper(index+1,coins,amount,cache)
            value = min(includeNext,includeCurrent,notInclude)
            cache[(index,amount)] = value
            return value
        answer= helper(0,coins,amount,cache)
        return answer if answer!=inf else -1
            

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
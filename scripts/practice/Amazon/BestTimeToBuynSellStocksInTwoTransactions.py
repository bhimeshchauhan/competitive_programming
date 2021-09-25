"""

Best Time to Buy and Sell Stock III - In At most two transaction

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. 
You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are 
engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:

Input: prices = [1]
Output: 0

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105

"""

# Intuition

"""

You want to make the most money that you can by completing two transactions. 
You can do this with one pass through the array. 
You have to keep track of three pieces of information:

- If I completed the best transaction until this point, 
how much money would I make (i.e. the first problem in the series).

- At which point can I acquire a second stock and keep the most money in my pocket. 
The money that I have will be firstProfit-secondPrice. 
(Note that this value could be negative, if the second stock costs more than you 
made from the first one. 
This is not a problem, as you will make that money back when you sell the second stock)

You can solve the problem in one iteration through the array. 
The way to accomplish this is to ask: If I do the best transaction until now and buy the 
second stock at the current price, will I end up with more money in my pocket than I 
would have in a previous stage of the iteration.

    mostMoneyInPocket = max(mostMoneyInPocket, firstTransactionProfit - currentPrice)

- What is the highest price that I can sell that second stock for? 
Since I already bought it all I have to do is find the highest 
price to sell it for.

- As you iterate, ask: if I sold it at the current price, 
would it make more money than selling it earlier?

    profitFromTwoTransactions = max(secondProfit, mostMoneyInPocket + currentPrice)

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyFirstStock = prices[0]
        sellFirstStockProfit = 0

        buySecondStock = -prices[0]
        profitFromTwoTransactions = 0

        for currentPrice in prices:
            buyFirstStock = min(buyFirstStock, currentPrice)
            sellFirstStockProfit = max(
                sellFirstStockProfit, currentPrice - buyFirstStock)

            buySecondStock = max(
                buySecondStock, sellFirstStockProfit - currentPrice)
            profitFromTwoTransactions = max(
                profitFromTwoTransactions, buySecondStock + currentPrice)

        return profitFromTwoTransactions

"""

Best Time to Buy and Sell Stock II

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:

1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4

"""

"""

Lets suppose there are two pointers left and right
The array is [ 7, 1, 5, 3, 6, 4 ]

Lets start the left pointer from 0th index and right pointer from 1st index.

So,
left=0
right=1

Now the algorithm is: If and only if the element at left is lesser than the element at right, find the profit

Step by step expanation is given below

When left=0, element is 7, and right=1, element is 1. Right element is smaller than left element. So we will not calculate the profit at all.
Increase both the left and right pointers by 1

When left=1, element is 1, and right=2, element is 5. Right element is greater than left element. So we will calculate the profit. Profit = 5 - 1 = 4.
Add the profit into a variable(s). Sum becomes 0+4=4
Increase both the left and right pointers by 1

When left=2, element is 5, and right=3, element is 3. Right element is lesser than left element. So we will not calculate the profit.
Increase both the left and right pointers by 1

When left=3, element is 3, and right=4, element is 6. Right element is greater than left element. So we will calculate the profit. Profit = 6 - 3 = 3.
Add the profit into a variable(s). Sum becomes 4+3=7
Increase both the left and right pointers by 1

When left=4, element is 6, and right=5, element is 4. Right element is lesser than left element. So we will not calculate the profit.
Increase both the left and right pointers by 1

Return the sum at the end which means it returns Sum=7


"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        s = 0
        while(right < len(prices)):
            if prices[left] < prices[right]:
                s += prices[right]-prices[left]
            left += 1
            right += 1
        return s

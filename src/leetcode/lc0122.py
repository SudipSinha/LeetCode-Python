"""Best Time to Buy and Sell Stock II

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """Time complexity: O(n), space complexity: O(1)."""
        profit__sum = 0
        for date_buy in range(len(prices) - 1):
            if prices[date_buy + 1] > prices[date_buy]:
                profit__sum += prices[date_buy + 1] - prices[date_buy]
        return profit__sum

"""Best Time to Buy and Sell Stock

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.
"""


class Solution:
    def maxProfit_naive(self, prices: list[int]) -> int:
        """Time complexity: O(n^2), space complexity: O(1)."""
        profit__max = 0
        for date_buy in range(len(prices) - 1):
            for date_sell in range(date_buy + 1, len(prices)):
                profit__cur = prices[date_sell] - prices[date_buy]
                if profit__cur > profit__max:
                    profit__max = profit__cur
        return profit__max

    def maxProfit_2ptr(self, prices: list[int]) -> int:
        """Time complexity: O(n), space complexity: O(1)."""
        profit__max = 0
        date_buy = 0
        for date_sell in range(1, len(prices)):
            if prices[date_sell] > prices[date_buy]:
                profit__cur = prices[date_sell] - prices[date_buy]
                profit__max = max(profit__cur, profit__max)
            else:
                date_buy = date_sell
        return profit__max

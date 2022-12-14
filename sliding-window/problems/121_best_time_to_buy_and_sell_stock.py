# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minN = float("inf")
        windowStart = maxProfit = 0
        while windowStart < len(prices) - 1:
            if prices[windowStart] < minN:
                minN = prices[windowStart]
                maxProfit = max(maxProfit, max(prices[windowStart + 1:]) - minN)
            windowStart += 1
        return maxProfit
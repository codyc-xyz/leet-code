# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = maxProfit = 0
        r = 1
        
        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit
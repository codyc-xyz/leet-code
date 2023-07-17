# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note:

# You may not engage in multiple transactions simultaneously(i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        buy_has_cache = [False] * N
        buy_cache = [None] * N

        sell_has_cache = [False] * N
        sell_cache = [None] * N

        def buy(day):
            if day == N:
                return 0
            if buy_has_cache[day]:
                return buy_cache[day]
            bought = sell(day + 1) - prices[day] - fee
            not_bought = buy(day + 1)
            best = max(bought, not_bought)
            buy_has_cache[day] = True
            buy_cache[day] = best
            return best

        def sell(day):
            if day == N:
                return 0
            if sell_has_cache[day]:
                return sell_cache[day]

            sold = buy(day + 1) + prices[day]
            not_sold = sell(day + 1)
            best = max(sold, not_sold)
            sell_has_cache[day] = True
            sell_cache[day] = best
            return best
        return buy(0)

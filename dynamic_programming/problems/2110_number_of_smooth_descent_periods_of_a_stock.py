# You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

# A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

# Return the number of smooth descent periods.

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = len(prices)
        for i in range(len(prices)):
            prev = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j] == prev - 1:
                    ans += 1
                    prev = prices[j]
                else:
                    break
        return ans

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = len(prices)
        seen = set()
        for i in range(len(prices)):
            if i in seen:
                continue
            prev = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j] == prev - 1:
                    ans += j-i
                    prev = prices[j]
                    seen.add(j)
                else:
                    break
        return ans

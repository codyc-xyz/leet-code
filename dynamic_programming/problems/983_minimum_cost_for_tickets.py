# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

# Train tickets are sold in three different ways:

# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.

# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        if len(days) == 1:
            return min(costs)
        dp = [c * costs[0] for c in range(1, len(days) + 1)]

        for i in range(1, len(days)):
            dp[i] = min(dp[i], dp[i-1] + costs[0])
            for j in range(0, i + 1):
                if days[i] - days[j] < 7:
                    dp[i] = min(dp[i], dp[j-1] + costs[1]
                                if j > 0 else costs[1])
                if days[i] - days[j] < 30:
                    dp[i] = min(dp[i], dp[j-1] + costs[2]
                                if j > 0 else costs[2])

        return dp[-1]

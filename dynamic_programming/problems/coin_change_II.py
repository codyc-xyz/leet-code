# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, rem):
            if (i, rem) in dp:
                return dp[(i, rem)]
            if rem == 0:
                return 1
            if i == len(coins) or rem < 0:
                return 0
            dp[(i, rem)] = 0
            for j in range(rem // coins[i] + 1):
                dp[(i, rem)] += dfs(i+1, rem - coins[i] * j)
            return dp[(i, rem)]
        return dfs(0, amount)
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, rem):
            if rem == 0:
                return 1
            if i == len(coins) or rem < 0:
                return 0
            res = 0
            for j in range(rem // coins[i] + 1):
                res += dfs(i+1, rem - coins[i] * j)
            return res
        return dfs(0, amount)
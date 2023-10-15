# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

# Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        mod = 10**9+7

        dp = defaultdict(int)
        dp[0, 0] = 1

        def dfs(pos, steps):
            if dp[pos, steps]:
                return dp[pos, steps]
            if steps == 0 or steps < pos:
                dp[pos, steps] = 0
                return 0
            waysToZero = 0

            waysToZero += dfs(pos, steps - 1)
            if pos < arrLen - 1:
                waysToZero += dfs(pos + 1, steps - 1)
            if pos > 0:
                waysToZero += dfs(pos - 1, steps - 1)
            dp[pos, steps] = waysToZero

            return waysToZero
        ans = dfs(0, steps) % mod
        return ans

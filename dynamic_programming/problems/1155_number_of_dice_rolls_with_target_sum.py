# You have n dice, and each dice has k faces numbered from 1 to k.

# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        cache = {}

        def dfs(N, rem):
            if rem < 0:
                return 0
            if (N, rem) in cache:
                return cache[(N, rem)]
            if rem == 0 and N == 0:
                return 1
            if N == 0:
                cache[(N, rem)] = 0
                return 0
            cache[(N, rem)] = 0
            for j in range(1, k+1):
                cache[(N, rem)] += dfs(N - 1, rem - j)
            return cache[(N, rem)]
        return dfs(n, target) % MOD


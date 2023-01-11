# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        K = k = 1
        while n > 0:
            n -= 1
            K -= 1
            if K == 0:
                k += 1
                K = k
                rows += 1
        return rows
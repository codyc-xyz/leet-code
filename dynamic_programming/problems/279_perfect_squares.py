# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

class Solution:
    def numSquares(self, n: int) -> int:
        
        perfSquares = []
        for i in range(1, n+1):
            if i **2 <= n:
                perfSquares.append(i**2)
            else:
                break

        perfSquares = perfSquares[::-1]
        cache = {}
        def dfs(N):
            if N == 0:
                return 0
            if N in cache:
                return cache[N]
            min_count = float('inf')
            for j in perfSquares:
                if N - j >= 0:
                    min_count = min(min_count, dfs(N-j) + 1)
            cache[N] = min_count
            return cache[N]
        return dfs(n)

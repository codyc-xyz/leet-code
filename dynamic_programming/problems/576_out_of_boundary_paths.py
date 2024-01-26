# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

class Solution:
    def findPaths(self, M: int, N: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        self.ans = 0

        def recurse(m, n, moves):
            if moves < 0:
                return
            if m < 0 or m == M or n < 0 or n == N:
                self.ans += 1
                return
            recurse(m + 1, n, moves - 1)
            recurse(m - 1, n, moves - 1)
            recurse(m, n + 1, moves - 1)
            recurse(m, n - 1, moves - 1)

        self.seen = set()
        recurse(startRow, startColumn, maxMove)
        return self.ans % MOD

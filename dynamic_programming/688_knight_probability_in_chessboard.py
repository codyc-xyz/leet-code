# On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

# A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

# The knight continues moving until it has made exactly k moves or has moved off the chessboard.

# Return the probability that the knight remains on the board after it has stopped moving.

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        self.numerator = 0
        self.denominator = 0

        def backtrack(r, c, K):
            if r >= n or c >= n or r < 0 or c < 0:
                self.denominator += 1
                return
            if K == 0:
                self.numerator += 1
                return
            backtrack(r+2, c+1, K - 1)
            backtrack(r+2, c-1, K - 1)
            backtrack(r+1, c+2, K - 1)
            backtrack(r+1, c-2, K - 1)
            backtrack(r-2, c-1, K - 1)
            backtrack(r-1, c+2, K - 1)
            backtrack(r-1, c-2, K - 1)
            backtrack(r-2, c+1, K - 1)
        backtrack(row, column, k)
        if not self.numerator:
            return 0
        if not self.denominator:
            return 1

        return self.numerator / (8**k)


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        dp = [[[0 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]

        def backtrack(r, c, K):
            if r >= n or c >= n or r < 0 or c < 0:
                return 0
            if K == 0:
                return 1
            if dp[r][c][K]:
                return dp[r][c][K]
            res = 0
            res += backtrack(r+2, c+1, K - 1)
            res += backtrack(r+2, c-1, K - 1)
            res += backtrack(r+1, c+2, K - 1)
            res += backtrack(r+1, c-2, K - 1)
            res += backtrack(r-2, c-1, K - 1)
            res += backtrack(r-1, c+2, K - 1)
            res += backtrack(r-1, c-2, K - 1)
            res += backtrack(r-2, c+1, K - 1)
            dp[r][c][K] = res
            return res
        if row < 0 or column < 0 or row >= n or column >= n:
            return 0
        if k == 0:
            return 1
        backtrack(row, column, k)
        return dp[row][column][k] / (8**k)

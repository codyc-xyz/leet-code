# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position(row, col) will be(row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[None] * ROWS for _ in range(COLS)]
        ans = float('inf')

        for i in range(COLS):
            dp[0][i] = matrix[0][i]
        for i in range(1, ROWS):
            for j in range(COLS):
                currMin = matrix[i][j] + dp[i-1][j]
                if j < COLS - 1:
                    currMin = min(currMin, dp[i - 1][j + 1] + matrix[i][j])
                if j > 0:
                    currMin = min(currMin, dp[i - 1][j - 1] + matrix[i][j])
                dp[i][j] = currMin

        return min(dp[-1][i] for i in range(COLS))


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        R = len(matrix)
        C = len(matrix[0])
        dp = [[[None] for _ in range(C)] for _ in range(R)]

        for i in range(R):
            dp[0][i] = matrix[0][i]

        for i in range(1, R):
            for j in range(C):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                elif j == C - 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1],
                                   dp[i-1][j+1]) + matrix[i][j]

        return min(dp[-1])

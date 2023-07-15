# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position(row, col) will be(row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = []

        def dfs(r, c):
            if c >= COLS or c < 0:
                return float('inf')
            if r == ROWS:
                return 0
            currSum = matrix[r][c]
            currSum += min(dfs(r+1, c-1), dfs(r+1, c), dfs(r+1, c+1))
            return currSum

        for i in range(COLS):
            dp.append(dfs(0, i))

        return min(dp)

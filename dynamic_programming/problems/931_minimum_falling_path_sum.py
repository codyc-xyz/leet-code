# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position(row, col) will be(row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        hm = {}
        dp = []

        def dfs(r, c, prevSum):
            if c >= COLS or c < 0:
                return float('inf')
            if r == ROWS:
                return 0
            if (r, c) in hm and hm[(r, c)] <= prevSum:
                return float('inf')
            else:
                hm[(r, c)] = prevSum
            currSum = matrix[r][c]
            currSum += min(dfs(r+1, c-1, prevSum + currSum), dfs(r+1,
                           c, prevSum + currSum), dfs(r+1, c+1, prevSum + currSum))
            return currSum

        for i in range(COLS):
            dp.append(dfs(0, i, 0))

        return min(dp)

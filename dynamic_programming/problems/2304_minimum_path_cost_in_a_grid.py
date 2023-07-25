# You are given a 0-indexed m x n integer matrix grid consisting of distinct integers from 0 to m * n - 1. You can move in this matrix from a cell to any other cell in the next row. That is, if you are in cell (x, y) such that x < m - 1, you can move to any of the cells (x + 1, 0), (x + 1, 1), ..., (x + 1, n - 1). Note that it is not possible to move from cells in the last row.

# Each possible move has a cost given by a 0-indexed 2D array moveCost of size(m * n) x n, where moveCost[i][j] is the cost of moving from a cell with value i to a cell in column j of the next row. The cost of moving from cells in the last row of grid can be ignored.

# The cost of a path in grid is the sum of all values of cells visited plus the sum of costs of all the moves made. Return the minimum cost of a path that starts from any cell in the first row and ends at any cell in the last row.

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)
        dp = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        hm = {}
        for i in range(len(moveCost)):
            for j in range(len(moveCost[0])):
                if i in hm:
                    hm[i].append([moveCost[i][j], j])
                else:
                    hm[i] = [[moveCost[i][j], j]]

        def dfs(r, c, cost):
            dp[r][c] = cost
            if r == ROWS - 1:
                return

            for i in range(len(hm[grid[r][c]])):
                currVal, nextCol = hm[grid[r][c]][i]
                if dp[r+1][nextCol] > cost + currVal + grid[r+1][nextCol]:
                    dfs(r+1, nextCol, cost + currVal + grid[r+1][nextCol])

        for c in range(COLS):
            dfs(0, c, grid[0][c])

        return min(dp[-1][c] for c in range(COLS))

# You are given a 0-indexed m x n matrix grid consisting of positive integers.

# You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

# From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
# Return the maximum number of moves that you can perform.

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = {(-1, 1), (0, 1), (1, 1)}
        self.ans = 0
        def dfs(x, y, moves):
            for dX, dY in dirs:
                currX = dX + x
                currY = dY + y
                if currX  >= 0 and currX < ROWS and currY >= 0 and currY < COLS and grid[x][y] < grid[currX][currY]:
                    dfs(currX, currY, moves + 1)
                self.ans = max(self.ans, moves)

        for i in range(ROWS):
            dfs(i, 0, 0)
        return self.ans

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = {(-1, 1), (0, 1), (1, 1)}
        seen = {}
        self.ans = 0
        def dfs(x, y, moves):
            for dX, dY in dirs:
                currX = dX + x
                currY = dY + y
                if currX  >= 0 and currX < ROWS and currY >= 0 and currY < COLS and grid[x][y] < grid[currX][currY] and (currX, currY) not in seen:
                    dfs(currX, currY, moves + 1)
                self.ans = max(self.ans, moves)
                seen[(x, y)]= moves


        for i in range(ROWS):
            dfs(i, 0, 0)
        return self.ans

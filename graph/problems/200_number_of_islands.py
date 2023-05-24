# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            seen.add((row, col))
            for l, r in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                if (l, r) not in seen and l >=0 and l < len(grid) and r >= 0 and r < len(grid[0]) and grid[l][r] == '1':
                    dfs(l, r)

            return 1
            


        ans = 0
        seen = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    ans += dfs(row, col)
        return ans

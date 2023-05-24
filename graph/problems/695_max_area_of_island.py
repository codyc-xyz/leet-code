# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxIsland = 0
        seen = set()
        def dfs(r, c):
            size = 1
            for row, col in ((r - 1, c), (r+1, c), (r, c-1), (r, c+1)):
                if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    size += dfs(row, col) 
            return size

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == 1:
                    seen.add((r, c))
                    maxIsland = max(maxIsland, dfs(r,c))
                
        return maxIsland
            
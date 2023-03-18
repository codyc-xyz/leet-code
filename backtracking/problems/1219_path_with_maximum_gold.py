# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

# Return the maximum amount of gold you can collect under the conditions:

# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        maxGold = 0

        def backtrack(i, j, currGold, path):
            self.gold = max(self.gold, currGold)
            if i >= row or i < 0 or j >= column or j < 0 or grid[i][j] == 0 or (i, j) in path:
                return
            path.add((i, j))
            currGold += grid[i][j]
            backtrack(i + 1, j, currGold, path)
            backtrack(i, j + 1, currGold, path)
            backtrack(i - 1, j, currGold, path)
            backtrack(i, j - 1, currGold, path)
            path.remove((i, j))
            currGold -= grid[i][j]
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] > 0:
                    self.gold = 0
                    backtrack(i, j, 0, set())
                    maxGold = max(maxGold, self.gold)
        
        return maxGold
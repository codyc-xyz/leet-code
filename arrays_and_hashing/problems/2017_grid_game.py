# You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

# Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

# At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. 
# Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

# The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. 
# If both robots play optimally, return the number of points collected by the second robot.

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        prefix1, prefix2 = [0], [0]
        
        for i in range(2):
            j = 0
            if i == 0:
                while j < len(grid[i]):
                    prefix1.append(prefix1[-1] + grid[i][j])
                    j += 1
            else:
                while j < len(grid[i]):
                    prefix2.append(prefix2[-1] + grid[i][j])
                    j += 1
       
        minScore = float("inf")
        for i in range(1, len(prefix1)):
            p2 = max(prefix1[-1] - prefix1[i], prefix2[i - 1])
            minScore = min(minScore, p2)
            
        return minScore
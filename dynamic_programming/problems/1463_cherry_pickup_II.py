# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:

# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.
 
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        cache = {}
        dirs = {(1,-1), (1, 0), (1,1)}
        def dfs(i1,j1,i2,j2):
            if i1 < 0 or j1 < 0 or i2 < 0 or j2 < 0 or i1 == ROWS or i2 == ROWS or j1 == COLS or j2 == COLS:
                return 0
            if (i1,j1,i2,j2) in cache:
                return cache[(i1,j1,i2,j2)]
            if i1==i2 and j1==j2:
                curr1=grid[i1][j1]
                curr2=0
            else:
                curr1=grid[i1][j1]
                curr2=grid[i2][j2]
            res=0
            for d1, d2 in dirs:
                for D1, D2 in dirs:
                    tmp = dfs(i1+d1,j1+d2, i2+D1,j2+D2)
                    if tmp > res:
                        res=tmp
            
            cache[(i1,j1,i2,j2)] = curr1+curr2+res
            return curr1+curr2+res
        return dfs(0,0,0,COLS-1)
 


            

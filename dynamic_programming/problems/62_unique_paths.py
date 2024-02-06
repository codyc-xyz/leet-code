# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            r = dfs(i, j+1)
            l = dfs(i+1, j)
            return r + l
        return dfs(0,0)
        

        
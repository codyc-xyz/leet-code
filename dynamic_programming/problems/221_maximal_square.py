# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = {}
        dirs = {(1, 0), (0, 1), (1, 1)}
        ans = 0
        def dfs(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            res = 0
            if matrix[r][c] == '1':
                res = float('inf')
                for dx, dy in dirs:
                    res = min(res, dfs(r+dx,c+dy) + 1)
            cache[(r,c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r,c))
        return ans**2 if ans > 0 else 0
                    
                

            

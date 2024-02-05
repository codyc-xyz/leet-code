# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        cols = [[] for _ in range(COLS)]
        rows = [[] for _ in range(ROWS)]
    
        for i in range(len(grid)):
            for j in range(len(grid)):
                rows[i].append(grid[i][j])
                cols[j].append(grid[i][j])

        ans = 0
        for r in rows:
            for c in cols:
                if r == c:
                    ans += 1
        return ans
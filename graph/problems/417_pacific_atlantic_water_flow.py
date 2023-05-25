# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(row, col, pac, atl, seen):
            seen.add((row, col))
            if row == 0 or col == 0:
                pac = True
            if row == ROWS - 1 or col == COLS - 1:
                atl = True
            if pac and atl:
                return [True, True]
            for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in seen and heights[row][col] >= heights[r][c]:
                    pac2, atl2 = dfs(r, c, pac, atl, seen)
                    pac = True if pac2 else pac
                    atl = True if atl2 else atl

            return [pac, atl]

        for r in range(ROWS):
            for c in range(COLS):
                pac, atl = dfs(r, c, False, False, set())
                if pac and atl:
                    res.append([r, c])
        return res
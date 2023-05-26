# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1  representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        rotten = collections.deque()
        fresh = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh.add((r, c))
        time = 0
        lenRotten = len(rotten)
        while rotten:
            curR, curC = rotten.popleft()
            for r, c in ((curR -1, curC), (curR+1, curC), (curR, curC-1), (curR, curC+1)):
                if (r, c) in fresh:
                    rotten.append((r, c))
                    fresh.remove((r, c))
            lenRotten -= 1
            if lenRotten == 0 and rotten:
                time += 1
                lenRotten = len(rotten)
        return time if not fresh else -1




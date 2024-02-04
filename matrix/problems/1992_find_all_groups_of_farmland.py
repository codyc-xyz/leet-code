# You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

# To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

# land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

# Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

class Solution:
    def findFarmland(self, graph: List[List[int]]) -> List[List[int]]:
        ROWS = len(graph)
        COLS = len(graph[0])
        seen = set()
        ans = []
        dirs = {(0, 1), (1, 0), (-1,0), (0,-1)}
        def dfs(x, y, res):
            if x < 0 or y < 0 or x == ROWS or y == COLS or (x, y) in seen or not graph[x][y]:
                return
            seen.add((x,y))
            res[0] = min(res[0], x)
            res[1] = min(res[1], y)
            res[2] = max(res[2], x)
            res[3] = max(res[3], y)
            for dx, dy in dirs:
                dfs(x+dx,y+dy, res)

        for r in range(ROWS):
            for c in range(COLS):
                if graph[r][c] and (r,c) not in seen:
                    res = [r,c,r,c]
                    dfs(r,c,res)
                    ans.append(res)
        return ans


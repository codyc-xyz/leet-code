# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        if grid[0][0]:
            return -1
        q = deque([(0, 0)])
        seen = set([(0, 0)])
        dirs = {(1,1), (0,1), (0,-1), (-1,0), (1,0), (-1,-1), (1,-1), (-1,1)}
        time = 1
        while q:
            lenQ = len(q)
            for i in range(lenQ):
                x, y = q.popleft()
                if x == ROWS - 1 and y == COLS - 1:
                    return time
                for dx, dy in dirs:
                    currX,currY = x+dx, y+dy
                    if currX >= 0 and currX < ROWS and currY >= 0 and currY < COLS and not grid[currX][currY] and (currX, currY) not in seen:
                        seen.add((currX, currY))
                        q.append((currX, currY))
            time += 1
        return -1

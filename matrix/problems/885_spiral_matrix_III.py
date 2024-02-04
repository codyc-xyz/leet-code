# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

# Return an array of coordinates representing the positions of the grid in the order you visited them.

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        self.totMoves = 1
        self.prev = 0
        ans = []
        def dfs(x,y,numMoves, i):
            if len(ans) == rows * cols:
                return
            if x > -1 and y > -1 and x < rows and y < cols:
                ans.append([x,y])
            if numMoves == 0:
                i += 1
                if i - self.prev == 2 or self.prev - i == 2:
                    self.prev = i
                    self.totMoves += 1
                if i == 4:
                    i = 0
                numMoves = self.totMoves

            currX,currY = dirs[i]
            dfs(x+currX,y+currY,numMoves - 1,i)
        dfs(rStart,cStart,1,0)
        return ans

            

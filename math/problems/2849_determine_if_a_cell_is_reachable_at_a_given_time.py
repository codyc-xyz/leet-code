# You are given four integers sx, sy, fx, fy, and a non-negative integer t.

# In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

# Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

# A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.

 

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        dirs = {(1,1), (1,0), (0,1), (-1,-1), (-1,0), (0,-1), (1, -1), (-1, 1)}

        seen = set()
        self.flag = False
        def dfs(x, y, T):
            if (x,y,T) in seen or self.flag or T < 0:
                return 
            seen.add((x,y,T))
            if x == fx and y == fy:
                self.flag = True
                return
            for dx, dy in dirs:
                dfs(x+dx,y+dy, T-1)
        if sx == fx and sy == fy and t < 2 and t != 0:
            return False
        dfs(sx,sy,t)
        return self.flag

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        dist = max(abs(fx-sx), abs(fy-sy))
        if dist == 0 and t == 1:
            return False
        return t >= dist

        


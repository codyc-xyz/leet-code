# There is an m x n grid, where (0, 0) is the top-left cell and (m - 1, n - 1) is the bottom-right cell. You are given an integer array startPos where startPos = [startrow, startcol] indicates that initially, a robot is at the cell (startrow, startcol). You are also given an integer array homePos where homePos = [homerow, homecol] indicates that its home is at the cell (homerow, homecol).

# The robot needs to go to its home. It can move one cell in four directions: left, right, up, or down, and it can not move outside the boundary. Every move incurs some cost. You are further given two 0-indexed integer arrays: rowCosts of length m and colCosts of length n.

# If the robot moves up or down into a cell whose row is r, then this move costs rowCosts[r].
# If the robot moves left or right into a cell whose column is c, then this move costs colCosts[c].
# Return the minimum total cost for this robot to return home.

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans = 0

        if startPos[0] <= homePos[0]:
            for i in range(startPos[0] + 1, homePos[0] + 1):
                ans += rowCosts[i]
        else:
            for i in range(startPos[0] - 1, homePos[0] - 1, -1):
                ans += rowCosts[i]
        if startPos[1] <= homePos[1]:
            for i in range(startPos[1] + 1, homePos[1] + 1):
                ans += colCosts[i]
        else:
            for i in range(startPos[1] - 1, homePos[1] - 1, -1):
                ans += colCosts[i]
                print(i)
        return ans
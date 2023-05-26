# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(row, col, path):
            if (row, col) in path:
                return True
            path.add((row, col))
            if 0 > row or row >= ROWS or 0 > col or col >= COLS:
                return False
            if board[row][col] == 'X':
                return True
        
            return dfs(row+1, col, path) and dfs(row-1, col, path) and dfs(row, col+1, path) and dfs(row, col-1, path)

        for r in range(ROWS):
            for c in range(COLS):
                path = set()
                if board[r][c] == 'O' and dfs(r, c, path):
                    for row, col in path:
                        board[row][col] = 'X'
        return board
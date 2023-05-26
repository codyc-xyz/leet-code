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

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(row, col, path):
            if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in path:
                return
            if board[row][col] == 'O':
                path.add((row, col))
                dfs(row+1, col, path)
                dfs(row-1, col, path)
                dfs(row, col+1, path)
                dfs(row, col-1, path)

        for r in range(ROWS):
            if board[r][0] == 'O':
                path = set()
                dfs(r, 0, path)
                for (r, c) in path:
                    board[r][c] = 'N'
            if board[r][COLS-1] == 'O':
                path = set()
                dfs(r, COLS-1, path)
                for (r, c) in path:
                    board[r][c] = 'N'

        for c in range(COLS):
            if board[0][c] == 'O':
                path = set()
                dfs(0, c, path)
                for (r, c) in path:
                    board[r][c] = 'N'
            if board[ROWS-1][c] == 'O':
                path = set()
                dfs(ROWS-1, c, path)
                for (r, c) in path:
                    board[r][c] = 'N'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'N':
                    board[r][c] = 'O'
        return board

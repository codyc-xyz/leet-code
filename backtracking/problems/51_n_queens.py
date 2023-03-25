# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for _ in range(n)]
        ans = []

        def conflict(row, col):
            for i in range(n):
                if board[row][i] == 'Q' or board[i][col] == 'Q':
                    return True
            for i, j in zip(range(row -1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return True
            
            for i, j in zip(range(row -1, -1, -1), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return True
            return False

        def backtrack(r, queens):
            if queens == 0:
                ans.append(["".join(row) for row in board])
                return
            if r >= n:
                return
            
            for c in range(n):
                if not conflict(r, c):
                    board[r][c] = 'Q'
                    backtrack(r + 1, queens - 1)
                    board[r][c] = '.'

        backtrack(0, n)
        return ans
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                j = board[r][c]
                if j == '.':
                    continue
                if j in columns[c] or j in rows[r] or j in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(j)
                columns[c].add(j)
                squares[(r // 3, c // 3)].add(j)
        return True
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(list)
        for r in board:
            i = 0
            vals = set()
            while i < len(r):
                if r[i].isdigit() == False:
                    columns[i].append('.')
                    i += 1
                    continue
                if r[i] in columns[i] or r[i] in vals:
                    return False
                columns[i].append(r[i])
                vals.add(r[i])
                i += 1
        
        squares = defaultdict(list)
        j = 0
        for r in columns.values():
            for i, c in enumerate(r):
                if c == '.':
                    continue
                elif 0 <= j <= 2:
                    if 0 <= i <= 2:
                        if c in squares[0]:
                            return False
                        squares[0].append(c)
                    if 3 <= i <= 5:
                        if c in squares[1]:
                            return False
                        squares[1].append(c)
                    if 6 <= i <= 8:
                        if c in squares[2]:
                            return False
                        squares[2].append(c)
                elif 3 <= j <= 5:
                    if 0 <= i <= 2:
                        if c in squares[3]:
                            return False
                        squares[3].append(c)
                    if 3 <= i <= 5:
                        if c in squares[4]:
                            return False
                        squares[4].append(c)
                    if 6 <= i <= 8:
                        if c in squares[5]:
                            return False
                        squares[5].append(c)
                elif 6 <= j <= 8:
                    if 0 <= i <= 2:
                        if c in squares[6]:
                            return False
                        squares[6].append(c)
                    if 3 <= i <= 5:
                        if c in squares[7]:
                            return False
                        squares[7].append(c)
                    if 6 <= i <= 8:
                        if c in squares[8]:
                            return False
                        squares[8].append(c)
            j += 1
        return True
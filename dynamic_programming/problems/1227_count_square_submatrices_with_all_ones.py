# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        ROWS, COLS = len(matrix), len(matrix[0])

        for col in range(COLS):
            count += matrix[0][col]

        for row in range(1, ROWS):
            count += matrix[row][0]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][j] == 1 and matrix[i-1][j] > 0 and matrix[i][j - 1] > 0 and matrix[i - 1][j- 1] > 0:
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                count += matrix[i][j]
        return count

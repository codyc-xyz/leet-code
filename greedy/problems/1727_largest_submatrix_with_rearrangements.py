# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        newMatrix = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if newMatrix[i][j]:
                    continue
                if matrix[i][j] == 1:
                    I = i
                    while I + 1 < rows and matrix[I + 1][j] == 1:
                        I += 1 
                    res = 1
                    while I >= i:
                        newMatrix[I][j] = res
                        I -= 1
                        res += 1
        ans = 0
        for r in newMatrix:
            r.sort(reverse=True)
            for j, c in enumerate(r):
                ans = max(ans, c * (j + 1))

        return ans


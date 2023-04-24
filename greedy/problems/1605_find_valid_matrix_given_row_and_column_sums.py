# You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

# Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

# Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        grid = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
            
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if rowSum[x] < colSum[y]:
                    val = rowSum[x]
                    grid[x][y] = val
                    rowSum[x] -= val
                    colSum[y] -= val
                else:
                    val = colSum[y]
                    grid[x][y] = val
                    colSum[y] -= val
                    rowSum[x] -= val
        return grid
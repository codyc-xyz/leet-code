# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = []
        for i in range(rowIndex + 1):
            rows.append([1] * (i + 1))

        for i in range(2, rowIndex + 1):
            for j in range(1, len(rows[i]) - 1):
                rows[i][j] = rows[i - 1][j - 1] + rows[i - 1][j]
        
        return rows[-1]
    
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        rows = []
        for i in range(rowIndex + 1):
            row = [1 for _ in range(i + 1)]
            rows.append(row)

        for i in range(2, rowIndex+1):
            for j in range(1, len(rows[i]) - 1):
                rows[i][j] = rows[i-1][j-1] + rows[i-1][j]

        return rows[-1]

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            triangle = [[1], [1, 1]]
        
        for i in range(2, numRows):
            row = []
            for i in range(len(triangle[-1]) + 1):
                if i == 0 or i == len(triangle[-1]):
                    row.append(1)
                else:
                    row.append(triangle[-1][i - 1] + triangle[-1][i])
            triangle.append(row)
        return triangle
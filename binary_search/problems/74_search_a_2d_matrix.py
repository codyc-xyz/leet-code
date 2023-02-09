# You are given an m x n integer matrix matrix with the following two properties:

# You are given an m x n integer matrix matrix with the following two properties:

# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = self.findRow(matrix, target) 
        return self.findTarget(matrix[row], target)
      
        
    def findTarget(self, row, target):
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True
        return False

    def findRow(self, matrix, target):
        l, r = 0, len(matrix) - 1
        end = len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target and matrix[m][end] >= target:
                return m
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][end] < target:
                l = m + 1
        return r
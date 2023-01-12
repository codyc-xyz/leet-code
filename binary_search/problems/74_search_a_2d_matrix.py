# You are given an m x n integer matrix matrix with the following two properties:

# You are given an m x n integer matrix matrix with the following two properties:

# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                return True
            
        row = r
        if row < len(matrix):
            l, r = 0, len(matrix[row]) - 1
        else:
            return False
        
        while l <= r:
            mid = (l + r) // 2
            
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
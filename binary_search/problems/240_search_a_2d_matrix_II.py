# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if bisect_right(matrix[i], target) != bisect_left(matrix[i], target):
                return True
        return False
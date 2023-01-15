# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            m = (l + r) // 2
            
            if sum(bisect_right(row, m) for row in matrix) < k:
                l = m + 1
            else:
                r = m
        return l
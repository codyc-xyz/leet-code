# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for r in grid:
            if r[-1] >= 0:
                continue
            neg += bisect_left(r[::-1], 0)
        return neg
# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
     
        pSum = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                pSum[i + 1][j + 1] = pSum[i+1][j] + pSum[i][j+1] - pSum[i][j] + mat[i][j]

        def maxSideLength(k):
            for i in range(m + 1 - k):
                for j in range(n + 1 - k):
                    if pSum[i+k][j+k] - pSum[i][j+k] - pSum[i+k][j] + pSum[i][j] <= threshold: 
                        return True 
            return False
        
        ans = 0
        l, r = 1, min(m,n)
        while l <= r:
            mid = (l + r) // 2
            if maxSideLength(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

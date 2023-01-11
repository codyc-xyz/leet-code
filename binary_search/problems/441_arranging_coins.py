# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l, r = 0, n
        
        while l <= r:
            mid = (l + r) // 2
            curr = mid * (mid + 1) // 2
            
            if n > curr:
                l = mid + 1
            elif n < curr:
                r = mid - 1
            else:
                return mid
        
        return (r + l) // 2

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        stairs = levels = 0
        for i in range(1, n + 1):
            stairs += i
            levels += 1
            
            if stairs > n:
                return levels - 1
            elif stairs == n:
                return levels
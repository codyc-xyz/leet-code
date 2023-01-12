# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
        
        for i in range(1, x + 1):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1
        return 0

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        
        while l <= r:
            mid = (l + r) // 2
            
            if mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
            else:
                return mid
        return (l + r) // 2
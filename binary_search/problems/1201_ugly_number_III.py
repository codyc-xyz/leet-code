# An ugly number is a positive integer that is divisible by a, b, or c.

# Given four integers n, a, b, and c, return the nth ugly number.

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        def numUglies(m):
            return (m // a + m // b + m // c) - (m // (ab) + m // (ac) + m // (bc)) + m // (abc)
            
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = a * bc // math.gcd(a, bc)
        
        l, r = 0, a * n  
        
        while l <= r:
            m = (l + r) // 2
            
            res = numUglies(m)
          
            if res >= n:
                r = m - 1
            else:
                l = m + 1
        return l
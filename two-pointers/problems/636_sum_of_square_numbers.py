# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        hm = {}
        
        while i * i <= c:
            hm[i * i] = i
            if c - i * i in hm:
                return True
            i += 1
        return False
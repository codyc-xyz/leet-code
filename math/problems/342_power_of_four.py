# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        curr = 1
        while curr <= n:
            if curr == n:
                return True
            curr *= 4
        return False

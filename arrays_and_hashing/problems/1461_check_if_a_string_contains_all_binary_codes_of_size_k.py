# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        l = 0
        for r in range(len(s) + 1):
            if r - l == k:
                code = s[l:r]
                codes.add(code)
                l += 1
    
        return len(codes) == 2**k
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1 = sorted(s1)
        length = len(s1)
        for windowStart in range(len(s2) - length + 1):
            if sorted(s2[windowStart:windowStart + length]) == s1:
                return True
        return False
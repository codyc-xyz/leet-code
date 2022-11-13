# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sort1 = sorted(s1)     
        windowEnd = len(s1) 
        sort2 = list(s2[:windowEnd])
        
        if sorted(sort2) == sort1:
            return True
        
        while windowEnd < len(s2):
            sort2.append(s2[windowEnd])
            sort2.pop(0)
            if sorted(sort2) == sort1:
                return True
            windowEnd += 1
        

            
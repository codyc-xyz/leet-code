# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmS = {}
        hmT = {}
        if len(s) != len(t):
            return False
        
        for i, c in enumerate(s):
            if c in hmS and hmS[c] != t[i] or t[i] in hmT and hmT[t[i]] != c:
                return False
            hmS[c] = t[i]
            hmT[t[i]] = c
        return True
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        l = 0
        for r in range(len(haystack)):
            if r - l == len(needle) - 1:
                if haystack[l:r + 1] == needle:
                    return l
                l += 1
        return -1
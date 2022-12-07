# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack) - len(needle) + 1:
            if haystack[i] == needle[0]:
                count = 0
                j = i
                for c in needle:
                    if j < len(haystack) and c == haystack[j]:
                        j += 1
                        count += 1
                if count == len(needle):
                    return j - len(needle)
            i += 1
        return - 1
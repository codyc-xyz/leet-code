# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
            
        a = 0
        for i in range(len(t)):
            if s[a] == t[i]:
                a += 1
            if a == len(s):
                return True
            if len(s) - a > (len(t) - i - 1):
                break
        return False
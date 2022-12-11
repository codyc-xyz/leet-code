# You are given two strings s and t consisting of only lowercase English letters.

# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for i in range(len(s)):
            if j == len(t):
                return 0
            elif s[i] == t[j]:
                j += 1
                
        return len(t) - j
# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        for i in range(1, N // 2 + 1):
            if N % i:
                continue
            if s[:i] * (N // i) == s:
                return True
        return False
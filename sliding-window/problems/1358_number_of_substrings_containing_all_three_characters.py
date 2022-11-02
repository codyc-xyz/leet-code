# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

class Solution:
    def unique(self, sub):
        if 'a' not in sub or 'b' not in sub or 'c' not in sub:
            return False
        return True

    def numberOfSubstrings(self, s: str) -> int:
        windowStart = count = 0
        for c in range(len(s)):
            windowEnd = windowStart + 2
            while windowEnd <= len(s):
                sub = s[windowStart:windowEnd]
                if self.unique(sub):
                    count += 1
                windowEnd += 1
            windowStart += 1
        return count

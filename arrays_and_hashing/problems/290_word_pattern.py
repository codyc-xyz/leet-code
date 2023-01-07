# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string = s.split(" ")
        if len(pattern) != len(string):
            return False
        hmP = {}
        hmS = {}
        for i,c in enumerate(string):
            if pattern[i] in hmP and hmP[pattern[i]] != c or c in hmS and hmS[c] != pattern[i]:
                return False
            elif pattern[i] not in hmP or c not in hmS:
                hmP[pattern[i]] = c
                hmS[c] = pattern[i]
        return True
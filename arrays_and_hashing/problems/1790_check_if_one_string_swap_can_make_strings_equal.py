# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        seen = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if len(seen) > 1:
                    return False
                else: 
                    seen.append(i)
        if len(seen) == 1:
            return False
        elif len(seen) == 0:
            return True
        return s1[seen[0]] == s2[seen[1]] and s1[seen[1]] == s2[seen[0]]
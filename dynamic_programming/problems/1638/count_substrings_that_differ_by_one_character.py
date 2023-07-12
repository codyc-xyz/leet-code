# Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

# For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.

# Return the number of substrings that satisfy the condition above.

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        if len(s) > len(t):
            s, t = t, s
        ans = 0
        N = len(s)
        M = len(t)
        for i in range(N):
            for j in range(M):
                count = 0
                for x in range(N):
                    if i + x >= N or j + x >= M:
                        break
                    if s[i+x] != t[j+x]:
                        count += 1
                        if count > 1:
                            break
                    if count == 1:
                        ans += 1
        return ans

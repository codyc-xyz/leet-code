# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        subsequences = set()
        
        for i, c in enumerate(s):
            j = i + 1
            chars = set()
            while j < len(s):
                if s[j] == s[i]:
                    outer = s[j]
                    for c in chars:
                        subsequences.add(outer + c + outer)
                chars.add(s[j])
                j += 1
        return len(subsequences)
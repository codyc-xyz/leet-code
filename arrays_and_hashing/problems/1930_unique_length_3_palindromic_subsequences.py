# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        subsequences = set()
        left = set()
        right = collections.Counter(s)
        
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]
                
            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    subsequences.add(c + s[i] + c)
            left.add(s[i])
        return len(subsequences)
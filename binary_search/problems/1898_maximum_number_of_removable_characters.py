# You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

# You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. 
# More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

# Return the maximum k you can choose such that p is still a subsequence of s after the removals.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        ans = 0
        l, r = 0, len(removable)
        while l < r:
            m = (l + r) // 2
            if self.removeSuccess(s, p, set(removable[:m + 1])):
                l = m + 1
            else:
                r = m
        return l

    def removeSuccess(self, S, P, removed):
        i = j = 0
        while i < len(S):
            if i in removed:
                i += 1
                continue
            if S[i] == P[j]:
                j += 1
                if j == len(P):
                    break
            i += 1
        return j == len(P)
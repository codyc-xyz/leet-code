# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        hm = {}
        for i,c in enumerate(s):
            hm[c] = i
        for i, c in enumerate(s):
            while stack and c not in stack and c < stack[-1] and hm[stack[-1]] > i:
                stack.pop()
            if c not in stack:
                stack.append(c)
        return "".join(stack)
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        wordDict = set(wordDict)

        def dfs(i, curr):
            if i == N and curr not in wordDict:
                return False
            if i == N and curr in wordDict:
                return True

            if curr in wordDict:
                return dfs(i + 1, s[i]) or dfs(i + 1, curr + s[i])

            return dfs(i + 1, curr + s[i])

        return dfs(0, "")


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        wordDict = set(wordDict)
        self.ans = False

        def dfs(i):
            if self.ans or i == N:
                self.ans = True
                return
            for w in wordDict:
                lenW = len(w)
                if i + lenW <= N and s[i:i+lenW] == w:
                    dfs(i + lenW)

        dfs(0)
        return self.ans


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        wordDict = set(wordDict)
        self.ans = False
        dp = [None for _ in range(N + 1)]

        def dfs(i):
            if self.ans or i == N:
                self.ans = True
                return
            for w in wordDict:
                lenW = len(w)
                if i + lenW <= N and s[i:i+lenW] == w and dp[i+lenW] != False:
                    dfs(i + lenW)
            dp[i] = False

        dfs(0)
        return self.ans

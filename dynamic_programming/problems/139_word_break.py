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

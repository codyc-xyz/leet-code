# You are given an array of n strings strs, all of the same length.

# We may choose any deletion indices, and we delete all the characters in those indices for each string.

# For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

# Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        compare = [True] * len(strs)

        for i in range(len(strs[0])):
            compareCols = compare[:]
            for j in range(1, len(strs)):
                if compareCols[j]:
                    if strs[j][i] < strs[j - 1][i]:
                        ans += 1
                        compare = compareCols
                        break
                    elif strs[j][i] > strs[j - 1][i]:
                        compare[j] = False
            if True not in compare:
                return ans

        return ans


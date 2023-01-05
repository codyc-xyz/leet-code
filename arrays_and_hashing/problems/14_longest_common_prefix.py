# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        minLen = float("inf")
        
        for s in strs:
            minLen = min(minLen, len(s))
        
        for i in range(minLen):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += s[i]
        return res
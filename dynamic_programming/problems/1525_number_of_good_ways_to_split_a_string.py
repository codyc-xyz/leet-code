# You are given a string s.

# A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

# Return the number of good splits you can make in s.

class Solution:
    def numSplits(self, s: str) -> int:
        currL = s[0]
        currR = s[1:]
        ans = 0
        for i in range(1, len(s)):
            if len(set(currL)) == len(set(currR)):
                ans += 1
            currR = currR[1:]
            currL += s[i]
        return ans

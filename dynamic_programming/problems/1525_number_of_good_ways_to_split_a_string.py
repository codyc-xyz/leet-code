# You are given a string s.

# A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

# Return the number of good splits you can make in s.

class Solution:
    def numSplits(self, s: str) -> int:
        rCount = {}
        lCount = {}
        for i in range(len(s)):
            if i == 0:
                lCount[s[i]] = 1
            else:
                if s[i] in rCount:
                    rCount[s[i]] += 1
                else:
                    rCount[s[i]] = 1
        ans = 0
        numL = 1
        numR = len(set(s[1:]))
        for i in range(1, len(s)):
            if numL == numR:
                ans += 1
            rCount[s[i]] -= 1
            if rCount[s[i]] == 0:
                del rCount[s[i]]
                numR -= 1
            if s[i] in lCount:
                lCount[s[i]] += 1
            else:
                lCount[s[i]] = 1
                numL += 1
        return ans

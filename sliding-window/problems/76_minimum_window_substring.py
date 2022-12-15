# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = collections.Counter(t)
        countS = defaultdict(int)
        seen = set()
        windowStart = 0
        minLen = float("inf")
        chars = len(set(t))
        r = 0
        for windowEnd, n in enumerate(s):
            countS[n] += 1
            
            if n not in seen and n in countT and countS[n] >= countT[n]:
                seen.add(n)
            else:
                continue
                
            while len(seen) == chars:
                if windowEnd - windowStart + 1 < minLen:
                    l, r = windowStart, windowEnd + 1
                    minLen = windowEnd - windowStart + 1
                countS[s[windowStart]] -= 1
                if s[windowStart] in countT and countS[s[windowStart]] < countT[s[windowStart]]:
                    seen.remove(s[windowStart])
                windowStart += 1
                
        if r != 0:
            return s[l:r]
        else:
            return ""
# You are given two strings s and t of the same length and an integer maxCost.

# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| 
# (i.e., the absolute difference between the ASCII values of the characters).

# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. 
# If there is no substring from s that can be changed to its corresponding substring from t, return 0.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        longest = windowStart = 0
        hm = {}
        for iS, cS in enumerate(s):
            hm[iS] = cS
        
        for iT, cT in enumerate(t):
            maxCost -= abs(ord(t[iT]) - ord(hm[iT]))
            
            while maxCost < 0:
                maxCost += abs(ord(t[windowStart]) - ord(hm[windowStart]))
                windowStart += 1
            longest = max(longest, iT - windowStart + 1)
        return longest
        


# You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

# A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

# Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. 
# If s is already balanced, return 0.

class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        windowStart = 0
        minLen = len(s)
        for windowEnd in range(len(s)):
            count[s[windowEnd]] -= 1
            while windowStart < len(s) and all(len(s) / 4 >= count[c] for c in 'QWER'):
                minLen = min(minLen, windowEnd - windowStart + 1)
                count[s[windowStart]] += 1
                windowStart += 1
                
        return minLen
            
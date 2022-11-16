# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        windowStart = maxLen = 0
        for windowEnd, c in enumerate(s):
            counter[c] += 1
            while counter[c] > 1:
                counter[s[windowStart]] -= 1
                windowStart += 1
            maxLen = max(maxLen, windowEnd - windowStart + 1)
        return maxLen
        
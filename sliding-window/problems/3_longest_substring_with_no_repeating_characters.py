# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        longest = windowStart = 0
        for windowEnd in range(len(s)):
            counter[s[windowEnd]] += 1
            if windowEnd - windowStart < max(counter.values()) + k:
                longest = windowEnd - windowStart + 1
            else:
                counter[s[windowStart]] -= 1
                windowStart += 1
        return longest
        
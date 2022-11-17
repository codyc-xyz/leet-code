# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        longest = windowStart = 0
        
        for windowEnd in range(len(s)):
            count[s[windowEnd]] += 1
            
            if windowEnd - windowStart < max(count.values()) + k:
                longest = max(longest, windowEnd - windowStart + 1)
            else:
                count[s[windowStart]] -= 1
                windowStart += 1
        return longest


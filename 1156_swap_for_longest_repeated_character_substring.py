# You are given a string text. You can swap two of the characters in the text.

# Return the length of the longest substring with repeated characters.

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        first, last = {}, {}
        ans, prev, count = 1, 0, 0
        
        for i in range(len(text)):
            if text[i] not in first:
                first[text[i]] = i
            last[text[i]] = i
        
        for i in range(len(text) + 1):
            if i < len(text) and text[i] == text[prev]:
                count += 1
            else:
                if first[text[prev]] < prev or last[text[prev]] > i:
                    count += 1
                ans = max(ans, count)
                count = 1
                prev = i
        def helper(item, before, after):
            count = 0
            while before >= 0 and text[before] == item:
                count += 1
                before -= 1
            while after < len(text) and text[after] == item:
                count += 1
                after += 1
            if first[item] <= before or last[item] >= after:
                count += 1
            return count
        
        for i in range(1, len(text) - 1):
            ans = max(ans, helper(text[i + 1], i - 1, i + 1))
        return ans
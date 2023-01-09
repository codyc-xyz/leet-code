# You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

# A string is called balanced if and only if:
# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.

# You may swap the brackets at any two indices any number of times.

# Return the minimum number of swaps to make s balanced.

class Solution:
    def minSwaps(self, s: str) -> int:
        l, r = 0, len(s) - 1
        swaps = opens = closes = 0
        while l < r:
            if s[l] == '[':
                opens += 1
            else:
                closes += 1
            if s[r] != '[':
                while r > l and s[r] != '[':
                    r -= 1
            if closes > opens:
                swaps += 1
                r -= 1
                opens += 1
                closes -= 1
            l += 1
        return swaps
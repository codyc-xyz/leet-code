# You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

# A string is called balanced if and only if:
# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.

# You may swap the brackets at any two indices any number of times.

# Return the minimum number of swaps to make s balanced.

class Solution:
    def minSwaps(self, s: str) -> int:
        
        stack = []
        
        for i, c in enumerate(s):
            if c == '[':
                stack.append(c)
            elif c == ']' and stack:
                stack.pop()
    
        return (len(stack) + 1) // 2
# You are given a binary string s and a positive integer k.

# A substring of s is beautiful if the number of 1's in it is exactly k.

# Let len be the length of the shortest beautiful substring.

# Return the lexicographically smallest beautiful substring of string s with length equal to len. If s doesn't contain a beautiful substring, return an empty string.

# A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b.

# For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.
 
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        length = float('inf')
        count = windowStart = 0

        for windowEnd in range(len(s)):
            if s[windowEnd] == '1':
                count += 1
                if count == k:
                    while windowStart <= windowEnd and count == k:
                        if s[windowStart] == '1':
                            count -= 1
                        windowStart += 1
                    curr = s[windowStart-1:windowEnd+1]
                    if windowEnd - windowStart < length:
                        ans = curr
                        length = windowEnd - windowStart
                    elif windowEnd - windowStart == length:
                        ans = min(ans, curr)
        return ans

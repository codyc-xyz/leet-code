# Given a string s, return the maximum number of ocurrences of any substring under the following rules:

# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = defaultdict(int)
        for i in range(len(s) - minSize + 1):
            sub = s[i:i+minSize]
            if len(set(sub)) <= maxLetters:
                d[sub] += 1
        return max(d.values()) if d else 0 
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub = s[:k]
        count = 0
        for i in range(k):
            if sub[i] == 'a' or sub[i] == 'e' or sub[i] == 'i' or sub[i] == 'o' or sub[i] == 'u':
                count += 1
        maxCount = count
        for c in range(k, len(s)):
            if s[c] == 'a' or s[c] == 'e' or s[c] == 'i' or s[c] == 'o' or s[c] == 'u':
                count += 1
            if s[c-k] == 'a' or s[c - k] == 'e' or s[c - k] == 'i' or s[c - k] == 'o' or s[c - k] == 'u':
                count -= 1
            maxCount = max(maxCount, count)
        return maxCount
        


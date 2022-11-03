# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub = s[:k]
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if sub[i] in vowels:
                count += 1
        maxCount = count
        for c in range(k, len(s)):
            if s[c] in vowels:
                count += 1
            if s[c-k] in vowels:
                count -= 1
            maxCount = max(maxCount, count)
        return maxCount
        


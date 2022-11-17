# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxCount = count = windowStart = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for windowEnd in range(len(s)):
            if s[windowEnd] in vowels:
                count += 1
            if windowEnd - windowStart + 1 == k:
                maxCount = max(maxCount, count)
                if s[windowStart] in vowels:
                    count -= 1
                windowStart += 1
        return maxCount
        


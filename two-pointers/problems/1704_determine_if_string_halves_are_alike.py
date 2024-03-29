# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        l, r = 0, len(s) // 2
        lVowels = rVowels = 0
        while r < len(s):
            if s[l] in vowels:
                lVowels += 1
            if s[r] in vowels:
                rVowels += 1
            l += 1
            r += 1

        return lVowels == rVowels

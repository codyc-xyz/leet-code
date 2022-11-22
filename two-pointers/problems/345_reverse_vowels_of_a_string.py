# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        a = list(s)
        left, right = 0, len(s) - 1
        
        while right > left:
            while left < right and s[left] not in vowels:
                left += 1
            while right > left and s[right] not in vowels:
                right -= 1
            a[left] = s[right]
            a[right] = s[left]
            left += 1
            right -= 1
        return "".join(a)
            
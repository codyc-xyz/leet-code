# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while right >= left:
            if s[right] != s[left]:
                string1 = s[:left] + s[left+1:]
                string2 = s[:right] + s[right+1:]
                return string1 == string1[::-1] or string2 == string2[::-1]
            right -= 1
            left += 1
        return True
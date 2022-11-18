# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        l = r = 0
        reverse = ""
        while l < len(s):
            while r < len(s) and s[r] != " ":
                r += 1
            reverse += s[l:r][::-1]
            if r < len(s) and s[r] == " ":
                reverse += " "
            l = r + 1
            r += 1
        return reverse
            
        
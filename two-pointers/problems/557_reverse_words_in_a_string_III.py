# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        left = right = 0
        reverse = ""
        while right < len(s):
            if s[right] == " " and left == 0:
                i = right - 1
                while i >= left:
                    reverse += s[i]
                    i -= 1
                left = right + 1
            elif s[right] == " ":
                i = right
                while i >= left:
                    reverse += s[i]
                    i -= 1
                left = right + 1
            elif right + 1 == len(s) and left == 0:
                i = right
                while i >= left:
                    reverse += s[i]
                    i -= 1
            elif right + 1 == len(s) and left != 0:
                reverse += " "
                i = right
                while i >= left:
                    reverse += s[i]
                    i -= 1
            right += 1    
        return reverse
            
        
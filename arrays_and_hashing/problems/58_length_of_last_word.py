# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split(' ')
        
        for s in split[::-1]:
            if s.isalpha():
                return len(s)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1
        length = 0
        
        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue
            else:
                while i >= 0 and s[i].isalpha():
                    i -= 1
                    length += 1
                return length
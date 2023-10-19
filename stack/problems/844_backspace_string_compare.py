# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stackS = []
        stackT = []
        
        for c in s:
            if c == '#':
                if stackS:
                    stackS.pop()
            else:
                stackS.append(c)
        
        for c in t:
            if c == '#':
                if stackT:
                    stackT.pop()
            else:
                stackT.append(c)
        
        return stackS == stackT
    

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stackS = []
        stackT = []
        i = j = 0
        while i < len(s) or j < len(t):
            if i < len(s):
                if s[i] == '#' and stackS:
                    stackS.pop()
                elif s[i] != '#':
                    stackS.append(s[i])
            if j < len(t):
                if t[i] == '#' and stackT:
                    stackT.pop()
                elif t[i] != '#':
                    stackT.append(t[j])
            i += 1
            j += 1
        return stackS == stackT

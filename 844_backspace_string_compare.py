# Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        resS = []
        resT = []
        
        for i in range(len(s)):
            if s[i] != '#':
                resS.append(s[i])
            else:
                if resS:
                    resS.pop()

        for i in range(len(t)):
            if t[i] != '#':
                resT.append(t[i])
            else:
                if resT:
                    resT.pop()
        return resS == resT
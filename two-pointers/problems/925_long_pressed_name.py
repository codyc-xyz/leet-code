# Your friend is typing his name into a keyboard. 
# Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        a = 0
        for i in range(len(typed)):
            if a < len(name) and typed[i] == name[a]:
                a += 1
            elif i == 0 or typed[i] != typed[i - 1]:
                return False
        return a == len(name)
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". 
# Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        s = t = 0
        length = len(start) 
        while s < length and t < length:
            while s < length and start[s] == 'X':
                s += 1
            while t < length and end[t] == 'X':
                t += 1
            if (s < length and t < length) and (start[s] == 'L' and s < t or start[s] == 'R' and s > t):
                return False
            s += 1
            t += 1
        return True
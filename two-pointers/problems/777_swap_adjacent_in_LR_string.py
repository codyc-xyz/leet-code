# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". 
# Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        
        if start.replace("X", "") != end.replace("X", ""):
            return False
        
        s = e = 0
        
        while s < n and e < n:
            while s < n and start[s] == "X":
                s += 1
            while e < n and end[e] == "X":
                e += 1
            if (s < n and (start[s] == "L" and s < e)) or (e < n and (start[s] == "R" and s > e)):
                return False
            s += 1
            e += 1
        return True
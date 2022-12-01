# You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.

# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.

# Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        s = t = 0
        length = len(start) 
        while s < length and t < length:
            while s < length and start[s] == '_':
                s += 1
            while t < length and target[t] == '_':
                t += 1
            if (s < length and t < length) and (start[s] == 'L' and s < t or start[s] == 'R' and s > t):
                return False
            s += 1
            t += 1
        return True
        
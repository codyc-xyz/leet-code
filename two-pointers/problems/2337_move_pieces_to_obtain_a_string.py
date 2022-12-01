# You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.

# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.

# Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start = list(start)
        target = list(target)
        filtered_start = [pos for pos in start if pos != '_']
        filtered_target = [pos for pos in target if pos != '_']
        left = []
        right = []
        if filtered_start != filtered_target:
            return False
        for i, n in enumerate(target):
            if n == 'L':
                left.append(i)
            if n == 'R':
                right.append(i)
        for i, n in enumerate(start):
            if n == 'L' and i < max(left):
                return False
            if n == 'R' and i > min(right):
                return False
        return True
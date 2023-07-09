# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        countS = collections.Counter(s)
        if s == goal:
            return max(countS.values()) > 1

        countG = collections.Counter(goal)
        if countS == countG:
            diffs = 0
            for i, j in zip(s, goal):
                if i != j:
                    diffs += 1
            return diffs == 2
        return False

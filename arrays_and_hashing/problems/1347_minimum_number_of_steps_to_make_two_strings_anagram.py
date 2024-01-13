# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different ( or the same) ordering.

class Solution:
    def minSteps(self, s: str, t: str) -> int:

        countS = collections.Counter(s)
        countT = collections.Counter(t)
        ans = 0

        for c in set(s):
            if countS[c] > countT[c]:
                ans += countS[c] - countT[c]

        return ans

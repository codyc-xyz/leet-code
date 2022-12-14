# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1 = sorted(s1)
        length = len(s1)
        for windowStart in range(len(s2) - length + 1):
            if sorted(s2[windowStart:windowStart + length]) == s1:
                return True
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            counter1[s1[i]] += 1
        
        for i in range(len(s1)):
            counter2[s2[i]] += 1
            
        if counter1 == counter2:
            return True
        windowStart, windowEnd = 0, len(s1)
        
        while windowEnd < len(s2):
            counter2[s2[windowStart]] -= 1
            if counter2[s2[windowStart]] == 0:
                del counter2[s2[windowStart]]
            counter2[s2[windowEnd]] += 1
            if counter1 == counter2:
                return True
            windowStart += 1
            windowEnd += 1
        return False
            
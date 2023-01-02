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
        
        for i, n in enumerate(s1):
            counter1[n] +=1 
        
        for i in range(len(s1)):
            counter2[s2[i]] += 1
        
        l, r = 0, len(s1)
        while r < len(s2):
            if counter1 == counter2:
                return True
            counter2[s2[r]] += 1
            counter2[s2[l]] -= 1
            if counter2[s2[l]] == 0:
                del counter2[s2[l]]
            r += 1
            l += 1
        return counter1 == counter2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        
        for i, c in enumerate(s1):
            d1[c] += 1
            
        windowStart = 0
        for i, c in enumerate(s2):
            d2[c] += 1
            
            while d2[c] > d1[c]:
                d2[s2[windowStart]] -= 1
                if d2[s2[windowStart]] == 0:
                    del d2[s2[windowStart]]
                windowStart += 1
            if d1 == d2:
                return True
        return False
            
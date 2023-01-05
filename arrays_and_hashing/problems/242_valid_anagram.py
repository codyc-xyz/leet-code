# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmS = {}
        hmT = {}
        
        for c in s:
            if c not in hmS:
                hmS[c] = 1
            else:
                hmS[c] += 1
            
        for c in t:
            if c not in hmT:
                hmT[c] = 1
            else:
                hmT[c] += 1
            
        return hmS == hmT

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = collections.Counter(s)
        countT = collections.Counter(t)
        
        return countS == countT
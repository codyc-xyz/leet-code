# Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
# You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        windowStart = 0
        anagrams = []
        counterP = defaultdict(int)
        counterWindow = defaultdict(int)
        for i in range(length):
            counterP[p[i]] += 1
        
        for i in range(length):
            if length <= len(s):
                counterWindow[s[i]] += 1
  
        for windowEnd in range(length, len(s) + 1):
            if counterP == counterWindow:
                anagrams.append(windowStart)
            if windowEnd < len(s):
                counterWindow[s[windowEnd]] += 1
            counterWindow[s[windowStart]] -= 1
            if counterWindow[s[windowStart]] <= 0:
                del counterWindow[s[windowStart]]
            windowStart += 1
        return anagrams
            


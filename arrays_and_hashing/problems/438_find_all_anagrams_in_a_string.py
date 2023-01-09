# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(p) > len(s):
            return ans
        countS = defaultdict(int)
        countP = defaultdict(int)
        for i in range(len(p)):
            countS[s[i]] += 1
            countP[p[i]] += 1
            
        l = 0
        if countS == countP:
            ans.append(l)
            
        for r in range(len(p), len(s)):
            if countS[s[l]] == 1:
                del countS[s[l]]
            else:
                countS[s[l]] -= 1
            countS[s[r]] += 1
            l += 1
            if countS == countP:
                ans.append(l)
        return ans
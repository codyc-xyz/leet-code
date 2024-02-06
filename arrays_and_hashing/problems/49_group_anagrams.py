# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)  
        for s in strs:
            ordered = sorted(s)
            res[tuple(ordered)].append(s)
        
        return res.values()
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in strs:
            st = sorted(s)     
            res[tuple(st)].append(s) 
        return res.values()


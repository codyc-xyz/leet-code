# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = collections.Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
    
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
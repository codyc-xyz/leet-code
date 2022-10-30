# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. 
# For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. 
# If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

class Solution:
     def isNice(self, sub):
        uniq = set(sub)
        for c in uniq:
            if c.lower() not in uniq or c.upper() not in uniq:
                return False
        return True
        
    def longestNiceSubstring(self, s: str) -> str:
        longestSubstring = ""
        windowStart, windowEnd = 0, 1
        for n in range(len(s)):
            while windowEnd <= len(s):
                sub = s[windowStart:windowEnd]
                if self.isNice(sub) and len(sub) > len(longestSubstring):
                    longestSubstring = sub
                windowEnd += 1
            windowStart += 1
            windowEnd = windowStart + 1
        return longestSubstring
                    
   
          


     
      

        

     

        


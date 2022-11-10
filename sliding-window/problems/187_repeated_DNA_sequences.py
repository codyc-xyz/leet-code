# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# For example, "ACGAATTCCG" is a DNA sequence.

# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 
# You may return the answer in any order.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = defaultdict(int)
        windowStart = 0
        uniq = set()
        
        if len(s) < 10:
            return None
        
        for windowEnd in range(9, len(s)):
            counter[s[windowStart:windowEnd]] += 1
            if counter[s[windowStart:windowEnd]] > 1:
                uniq.add(s[windowStart:windowEnd])
            windowStart += 1
        
                
        return uniq
                
        
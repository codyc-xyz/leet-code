# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 11:
            return []
        ans = set()
        hm = {}
        sequence = deque()
        for i in range(10):
            sequence.append(s[i])
            
        hm["".join(sequence)] = 1
        for i in range(10, len(s)):
            sequence.popleft()
            sequence.append(s[i])
            
            string = "".join(sequence)
            
            if string in hm:
                ans.add(string)
            else:
                hm[string] = 1
        return ans
      
    class Solution:
      def findRepeatedDnaSequences(self, s: str) -> List[str]:
          
          if len(s) < 11:
              return None
          counter = defaultdict(int)
          l = 0
          sequences = set()
          
          for r in range(10, len(s) + 1):
              sub = s[l:r]
              counter[sub] += 1
              if counter[sub] == 2:
                  sequences.add(sub)
              l += 1
          return sequences
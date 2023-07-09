# The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

# Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def largestVariance(self, s: str) -> int:
        maxSum = 0
        dp = [0] * 26
        start = ord('a')
        for i in range(26):
            for j in range(26):
                if i == j:
                    continue  
                for n in range(len(s)):
                    seen = False
                    currSum = 0
                    for k in range(n, len(s)):
                        if s[k] == chr(start + i):
                            currSum += 1
                        elif s[k] == chr(start + j):
                            currSum -= 1
                            seen = True
                        if seen:
                            maxSum = max(maxSum, currSum)
        return maxSum

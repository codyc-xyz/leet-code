# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.

# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

# The string is called alternating if no two adjacent characters are equal.

# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

class Solution:
    def minFlips(self, s: str) -> int:
        option1 = []
        option2 = []
        s2 = s + s
        
        for i in range(len(s2)):
            if i % 2 == 0:
                option1.append('0')
                option2.append('1')
            else:
                option1.append('1')
                option2.append('0')
        
        diff1 = diff2 = 0
        for i, n in enumerate(s):
            if n != option1[i]:
                diff1 += 1
            if n != option2[i]:
                diff2 += 1
                
        minDiff1 = diff1
        minDiff2 = diff2
        l, r = 0, len(s)
        while r < len(s2):
            if s2[r] != option1[r]:
                diff1 += 1
            if s2[r] != option2[r]:
                diff2 += 1
            if s2[l] != option1[l]:
                diff1 -= 1
            if s2[l] != option2[l]:
                diff2 -= 1
            minDiff1 = min(minDiff1, diff1)
            minDiff2 = min(minDiff2, diff2)
            r += 1
            l += 1
    
        return min(minDiff1, minDiff2)
# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
# It has a length of k.
# It is a divisor of num.
# Given integers num and k, return the k-beauty of num.
# Note:
#Leading zeros are allowed.
# 0 is not a divisor of any value.
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def isBeauty(self, n, num, length, k): 
        if n != 0 and num % n == 0 and length == k:
            return 1
        else:
            return 0
            
            
        
    
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        string = str(num)
        windowStart, windowEnd = 0, 1
        for c in range(len(string)):
            while windowEnd <= len(string):
                sub = string[windowStart:windowEnd]
                count += self.isBeauty(int(sub), num, len(sub), k)
                windowEnd += 1
            windowStart += 1
            windowEnd = windowStart + 1
        
        return count
            


# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
# It has a length of k.
# It is a divisor of num.
# Given integers num and k, return the k-beauty of num.
# Note:
#Leading zeros are allowed.
# 0 is not a divisor of any value.
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def isBeauty(self, n, num): 
        if n != 0 and num % n == 0: 
            return 1
        else:
            return 0
            
            
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        string = str(num)
        for windowStart in range(len(string)):
            sub = string[windowStart:windowStart + k]
            if len(sub) != k:
                break
            count += self.isBeauty(int(sub), num)
            windowStart += 1
            
        return count

  # O(N) time complexity


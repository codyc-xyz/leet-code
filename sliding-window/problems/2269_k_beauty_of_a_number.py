# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
# It has a length of k.
# It is a divisor of num.
# Given integers num and k, return the k-beauty of num.
# Note:
#Leading zeros are allowed.
# 0 is not a divisor of any value.
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums = str(num)
        count = windowStart = 0
        for windowEnd in range(len(nums) + 1):
            if windowEnd - windowStart == k:
                n = int(nums[windowStart:windowEnd])
                if n and num % n == 0:
                    count += 1
                windowStart += 1
        return count


# You are given an array nums consisting of positive integers.

# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

# Return the length of the longest nice subarray.

# A subarray is a contiguous part of an array.

# Note that subarrays of length 1 are always considered nice.

class Solution:
    def isNice(self, sub, n):
        if len(sub) >= 1:
            for c in sub:
                if n & c != 0:
                    return False
        return True
    
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest = windowStart = 0
        sub = []
        for windowEnd, n in enumerate(nums):
            while self.isNice(sub, n) == False:
                sub.pop(0)
                windowStart += 1
            sub.append(n)
            longest = max(longest, windowEnd - windowStart + 1)
        return longest

class Solution:
    def isNice(self, sub, n):
        if len(sub) >= 1:
            for c in sub:
                if n & c != 0:
                    return False
        return True
    
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest = 0
        sub = deque()
        for i, n in enumerate(nums):
            while self.isNice(sub, n) == False:
                sub.popleft()
            sub.append(n)
            longest = max(longest, len(sub))
        return longest
            
                
                
            
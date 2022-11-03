# Given an integer array nums and two integers firstLen and secondLen, 
# return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
# The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.
# A subarray is a contiguous part of an array.

class Solution:
    
    def findMax(self, nums, firstLen, secondLen):
        max1 = sum1 = sum(nums[:firstLen])
        sum2 = sum(nums[firstLen:firstLen + secondLen])
        cumMax = max1 + sum2
        
      
        for i in range(firstLen + secondLen, len(nums)):
            sum1 += nums[i - secondLen] - nums[i - firstLen - secondLen]
            sum2 += nums[i] - nums[i - secondLen]
            max1 = max(max1, sum1)
            cumMax = max(cumMax, max1+sum2)
        return cumMax
    
    
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:    
        return max(self.findMax(nums, firstLen, secondLen), self.findMax(nums, secondLen, firstLen))



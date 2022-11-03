# Given an integer array nums and two integers firstLen and secondLen, 
# return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
# The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.
# A subarray is a contiguous part of an array.

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:    
        
        res = firstMaxSum = secondMaxSum = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i2 in range(firstLen, len(nums) - secondLen):
            secondWindowSum = nums[i2 + secondLen] - nums[i2]
            firstMaxSum = max(firstMaxSum, nums[i2] - nums[i2 - firstLen])
            res = max(res, secondWindowSum + firstMaxSum)
            
        for i3 in range(secondLen, len(nums) - firstLen):
            firstWindowSum = nums[i3 + firstLen] - nums[i3]
            secondMaxSum = max(secondMaxSum, nums[i3] - nums[i3 - secondLen])
            res = max(res, firstWindowSum + secondMaxSum)
        return res






# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        smallestAt = [[None] for _ in range(len(nums))]
        largestAt = [[None] for _ in range(len(nums))]
        minNum = float('inf')
        maxNum = float('-inf')
        for i in range(len(nums)):
            minNum = min(minNum, nums[i])
            smallestAt[i] = minNum
        
        for i in range(len(nums) - 1, -1, -1):
            maxNum = max(maxNum, nums[i])
            largestAt[i] = maxNum

        for i, n in enumerate(nums):
            if n < largestAt[i] and n > smallestAt[i]:
                return True
        return False

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n1 = n2 = float('inf')
        for n in nums:
            if n > n2:
                return True
            if n > n1:
                n2 = min(n, n2)
            n1 = min(n, n1)
        return False


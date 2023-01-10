# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        digits = set(nums)
        
        for i in range(1, len(nums) + 2):
            if i not in digits:
                return i
        return 0
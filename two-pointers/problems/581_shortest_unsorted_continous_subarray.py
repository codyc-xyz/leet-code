# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1
            
        if left == len(nums) - 1:
            return 0
            
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
            
        minN = min(nums[left:right + 1])
        maxN = max(nums[left:right + 1])
        
        while left > 0 and nums[left - 1] > minN:
            left -= 1
            
        while right < len(nums) - 1 and nums[right + 1] < maxN:
            right += 1
            
    
        return right - left + 1
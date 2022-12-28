# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ramp = 0
        decrease = []
        increase = []
        j = len(nums) - 1
    
        for i, n in enumerate(nums):
            if not decrease or n < decrease[-1][0]:
                decrease.append([n, i])
                
        for i, n in enumerate(nums[::-1]):
            if not increase or n > increase[-1][0]:
                increase.append([n, j - i])
        
        dec = 0
        for i in range(len(increase) - 1, -1, -1):
            while increase[i][0] < decrease[dec][0]:
                dec += 1
            ramp = max(ramp, increase[i][1] - decrease[dec][1])
        
        return ramp
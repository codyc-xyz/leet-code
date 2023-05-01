# You are given an integer array nums.

# In one move, you can choose one element of nums and change it to any value.

# Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            return 0
        nums.sort()
        numMins = nums[:-3]
        numMaxs = nums[3:]
        numMinMax1 = nums[1:] + nums[:-2]
        numMinMax2 = nums[2:] + nums[:-1]
        return min(numMins[-1] - numMins[0], numMaxs[-1] - numMaxs[0], numMinMax1[-1] - numMinMax1[0], numMinMax2[-1] - numMinMax2[0])
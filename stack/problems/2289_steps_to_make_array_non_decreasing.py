# You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

# Return the number of steps performed until nums becomes a non-decreasing array.

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = [[nums[-1], 0]]
        ans = 0
        
        for i in range(len(nums) -2, -1, -1):
            count = 0
            while stack and nums[i] > stack[-1][0]:
                count = max(count + 1, stack.pop()[1])
            ans = max(ans, count)
            stack.append([nums[i], count])
        return ans
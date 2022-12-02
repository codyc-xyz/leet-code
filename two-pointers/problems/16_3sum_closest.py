# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        hm = {}
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            curr = 0
            while right > left:
                curr = nums[i] + nums[left] + nums[right]
                hm[curr] = abs(curr-target)
                if curr > target:
                    right -= 1
                else:
                    left += 1
        return min(hm, key = hm.get)
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        prevSum = float("inf")
        ans = float("inf")
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            curr = 0
            while right > left:
                curr = nums[i] + nums[left] + nums[right]
                if abs(curr-target) < prevSum:
                    prevSum = abs(curr - target)
                    ans = curr
                if curr > target:
                    right -= 1
                elif curr < target:
                    left += 1
                else:
                    return curr
        return ans
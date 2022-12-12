# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. 
# You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        minDiff = float("inf")
        while r < len(nums):
            minDiff = min(minDiff, nums[r] - nums[l])
            r += 1
            l += 1
        return minDiff






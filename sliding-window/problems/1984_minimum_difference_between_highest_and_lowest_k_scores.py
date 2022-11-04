# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. 
# You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        numbers = sorted(nums)
        windowStart, windowEnd = 0, k - 1
        minDiff = float("inf")
        while windowEnd < len(numbers):
            minDiff = min(minDiff, numbers[windowEnd] - numbers[windowStart])
            windowEnd += 1
            windowStart += 1
        return minDiff

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ordered = sorted(nums)
        minRes = float("inf")
        k -= 1
        for i in range(len(nums) - k):
            minRes = min(minRes, ordered[i+k] - ordered[i])
        return minRes






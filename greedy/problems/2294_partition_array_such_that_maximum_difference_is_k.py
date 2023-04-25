# You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

# Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()
        i = passes = 0
        while i < len(nums):
            anchor = nums[i] + k
            while i < len(nums) and nums[i] <= anchor:
                i += 1
            passes += 1

        return passes

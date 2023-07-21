# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        lenIncreasing = defaultdict(int)

        def backtrack(i, prev, length):
            if i == N:
                lenIncreasing[length] += 1
                return
            if nums[i] > prev:
                backtrack(i + 1, nums[i], length + 1)
            backtrack(i + 1, prev, length)

        backtrack(0, float('-inf'), 0)
        return lenIncreasing[max(lenIncreasing)]

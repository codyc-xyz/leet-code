# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if len(nums) < 3:
            return 0

        ans = 0
        for i in range(N - 2):
            curr = nums[i]
            currDiff = nums[i] - nums[i+1]
            res = 1
            for j in range(i + 1, N):
                if curr - nums[j] == currDiff:
                    res += 1
                    if res > 2:
                        ans += 1
                    curr = nums[j]
                else:
                    break

        return ans

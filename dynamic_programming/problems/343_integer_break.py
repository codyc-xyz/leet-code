# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        nums = [0, 1, 2, 3]
        for i in range(4, n+1):
            nums.append(max(nums[i - 3] * 3, nums[i - 2] * 2))
        return nums[-1]

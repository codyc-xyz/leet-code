# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        mod = 10**9+7
        while l <= r and nums[l] * 2 <= target:
            
            while nums[l] + nums[r] > target:
                r -= 1
            ans += pow(2, r - l, mod)
            ans %= mod
            l += 1
        return ans
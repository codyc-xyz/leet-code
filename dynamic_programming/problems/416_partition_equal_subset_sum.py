# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2:
            return False
        @cache
        def dfs(i, curr):
            if i == len(nums) or curr > total / 2:
                return False
            elif curr == total // 2:
                return True
            if dfs(i+1,curr):
                return True
            if dfs(i+1, curr+nums[i]):
                return True
        return dfs(0, 0)
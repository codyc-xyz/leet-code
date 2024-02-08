# You are given a 0-indexed array of integers nums, and an integer target.

# Return the length of the longest subsequence of nums that sums up to target. If no such subsequence exists, return -1.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(i, currSum, steps):
            if currSum == target:
                return steps
            if i == len(nums) or currSum > target:
                return 0

            take = dfs(i+1, currSum + nums[i], steps + 1)
            nTake = dfs(i+1, currSum, steps)
            return max(take, nTake)
        ans = dfs(0, 0, 0) 
        return ans if ans else -1
    
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(i, currSum):
            if currSum == target:
                return 0
            if i >= len(nums) or currSum > target:
                return -1001
            return max(1+dfs(i+1, currSum+nums[i]), dfs(i+1,currSum))
            
        ans = dfs(0, 0)
        dfs.cache_clear() 
        return ans if ans > 0 else -1

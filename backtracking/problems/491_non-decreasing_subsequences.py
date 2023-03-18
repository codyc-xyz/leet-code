# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def backtrack(i, path):
            if len(path) > 1 and path not in ans:
                ans.append(path)
            if i >= len(nums):
                return
            if not path or nums[i] >= path[-1]:
                backtrack(i + 1, path + [nums[i]])
            backtrack(i + 1, path)
        backtrack(0, [])
        return ans
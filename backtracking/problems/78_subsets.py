# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        def backtrack(nums, path, i):
            if i >= len(nums):
                return
            backtrack(nums, path[:], i + 1)
            path.append(nums[i])
            if path not in subsets:
                subsets.append(path)
            backtrack(nums, path[:], i + 1)

        for i in range(len(nums)):
            backtrack(nums[i:], [], i)

        return subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        path = []
        def backtrack(i):
            if i >= len(nums):
                subsets.append(path[:])
                return
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
            backtrack(i + 1)
        backtrack(0)
        return subsets
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(i, path):
            if i >= len(nums):
                if path not in ans:
                    ans.append(path)
                return
            path.append(nums[i])
            backtrack(i + 1, path[:])
            path.pop()
            backtrack(i + 1, path[:])
        backtrack(0, [])
        return ans
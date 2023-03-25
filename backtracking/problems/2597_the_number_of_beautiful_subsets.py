# You are given an array nums of positive integers and a positive integer k.

# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

# Return the number of non-empty beautiful subsets of the array nums.

# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def backtrack(i, path):
            if i == len(nums):
                for j in path:
                    if j - k in path:
                        return 0
                return 1 if path else 0

            return backtrack(i + 1, path + [nums[i]]) + backtrack(i + 1, path)

        return backtrack(0, [])
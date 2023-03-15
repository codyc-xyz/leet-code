# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(i, k, subSum):
            if k == 0:
                return True
            if subSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or subSum + nums[j] > target or (j > 0 and nums[j] == nums[j - 1] and not used[j - 1]):
                    continue
                used[j] = True
                if backtrack(j + 1, k, subSum + nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0, k, 0)
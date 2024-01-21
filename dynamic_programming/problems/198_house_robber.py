# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.ans = 0

        def recurse(i, currSum, tookAdj):
            if i == len(nums):
                self.ans = max(self.ans, currSum)
                return
            if tookAdj:
                recurse(i + 1, currSum, False)
            else:
                recurse(i+1, currSum + nums[i], True)
                recurse(i+1, currSum, False)

        recurse(0, 0, False)
        return self.ans


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i+1] = max((dp[i-1] + nums[i], dp[i]))

        return dp[-1]

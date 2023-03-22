# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        self.ans = 0
        def backtrack(i, target):
            if i == len(nums):
                if target == 0:
                    self.ans += 1
                return

            backtrack(i + 1, target - nums[i])
            backtrack(i + 1, target + nums[i])
        backtrack(0, target)
        return self.ans
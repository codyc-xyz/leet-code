# You are given a 0-indexed integer array nums of length n.

# nums contains a valid split at index i if the following are true:

# The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pSum = [0]
        ans = 0
        for n in nums:
            pSum.append(pSum[-1] + n)

        for i in range(1, len(pSum) - 1):
            if pSum[i] >= pSum[-1] - pSum[i]:
                ans += 1
        return ans
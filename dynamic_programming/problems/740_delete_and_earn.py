# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        count = collections.Counter(nums)
        N = max(nums)
        dp = [0 for _ in range(N+1)]
        dp[1] = count.get(1, 0)
        for n in range(2, N+1):
            dp[n] = max(dp[n-1], dp[n-2] + (n * count[n]))

        return dp[N]



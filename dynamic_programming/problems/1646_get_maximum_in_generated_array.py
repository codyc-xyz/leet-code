# You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# Return the maximum integer in the array nums​​​.

class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        dp = [0] * (n + 1)

        if n == 0:
            return 0
        
        dp[1] = 1

        for i in range(n + 1):
            if 2 <= 2 * i <= n:
                dp[i * 2] = dp[i]
            if 2 <= 2 * i + 1 <= n:
                dp[2 * i + 1] = dp[i] + dp[i + 1]
 
        return max(dp)
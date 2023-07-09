# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr) 
        dp = [0] * (N + 1)

        for i in range(1, N + 1):
            currMax = 0
            for j in range(1, min(i, k) + 1):
                currMax = max(currMax, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + currMax * j)
        return dp[N]
                
        

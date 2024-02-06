# You are given a positive integer array nums.

# Partition nums into two arrays, nums1 and nums2, such that:

# Each element of the array nums belongs to either the array nums1 or the array nums2.
# Both arrays are non-empty.
# The value of the partition is minimized.
# The value of the partition is |max(nums1) - min(nums2)|.

# Here, max(nums1) denotes the maximum element of the array nums1, and min(nums2) denotes the minimum element of the array nums2.

# Return the integer denoting the value of such partition.

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        dp = [float('inf') for _ in range(N)]

        for i in range(1, N):
            dp[i] = min(dp[i-1], nums[i] - nums[i-1])
            
        return dp[-1]
    
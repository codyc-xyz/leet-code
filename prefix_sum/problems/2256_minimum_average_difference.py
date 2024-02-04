# You are given a 0-indexed integer array nums of length n.

# The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

# Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

# Note:

# The absolute difference of two numbers is the absolute value of their difference.
# The average of n elements is the sum of the n elements divided (integer division) by n.
# The average of 0 elements is considered to be 0.

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        minAvgDiff = float('inf')
        pSum = [0]
        ans = 0
        for n in nums:
            pSum.append(pSum[-1] + n)

        for i in range(1, N + 1):
            l = int(pSum[i] / i)
            if N-i == 0:
                r = 0
            else:
                r = int((pSum[-1] - pSum[i]) / (N - i))
            curr = abs(l-r)
            if curr < minAvgDiff:
                ans = i - 1
                minAvgDiff = curr

      
        return ans


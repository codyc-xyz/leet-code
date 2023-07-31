# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

# For example, the product difference between(5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs(nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

# Return the maximum such product difference.

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        maxVal = scndMaxVal = float('-inf')
        minVal = scndMinVal = float('inf')
        for n in nums:
            if n > maxVal:
                scndMaxVal = maxVal
                maxVal = n
            elif n > scndMaxVal:
                scndMaxVal = n

            if n < minVal:
                scndMinVal = minVal
                minVal = n
            elif n < scndMinVal:
                scndMinVal = n

        return (maxVal * scndMaxVal) - (minVal * scndMinVal)

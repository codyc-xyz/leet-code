# You are given two positive integer arrays nums1 and nums2, both of length n.

# The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

# You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

# Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

# |x| is defined as:
# x if x >= 0, or
# -x if x < 0.

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        diff = []
        mod = 10**9 + 7
        res = float("inf")
        for i in range(len(nums1)):
            diff.append(abs(nums1[i] - nums2[i]))
        
        total = sum(diff)
        nums1.sort()
        for i in range(len(nums2)):
            idx = bisect_left(nums1, nums2[i])
        
            if idx > 0:
                res = min(res, total - diff[i] + abs(nums2[i] - nums1[idx - 1]))
                          
            if idx < len(nums1):
                res = min(res, total - diff[i] + abs(nums2[i] - nums1[idx]))
            
        return res % mod
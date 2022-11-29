# You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

# A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

# Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

# An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = ans = 0
        
        while p1 < len(nums1) and p2 < len(nums2):
            
            if nums1[p1] > nums2[p2]:
                p1 += 1
            else:
                ans = max(ans, p2 - p1)
                p2 += 1
        return ans
        
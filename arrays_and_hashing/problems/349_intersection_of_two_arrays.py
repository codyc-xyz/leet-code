# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N1 = set(nums1)
        N2 = set(nums2)
        ans = []
        for n in N1:
            if n in N2:
                ans.append(n)
        return ans
        
        
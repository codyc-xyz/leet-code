# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        res = []
        if len(nums1) > len(nums2):
            for i in range(len(nums2)):
                hm[nums2[i]] = i
            for i in range(len(nums1)):
                if nums1[i] in hm:
                    res.append(nums1[i])
        else:
            for i in range(len(nums1)):
                hm[nums1[i]] = i
            for i in range(len(nums2)):
                if nums2[i] in hm:
                    res.append(nums2[i])
            
        return set(res)
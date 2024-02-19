# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        seen = set()

        for n in nums1:
            seen.add(n)
        for n in nums2:
            if n in seen:
                return n
        return -1
    
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        f1 = f2 = 0

        while f1 < len(nums1) and f2 < len(nums2):
            if nums1[f1] > nums2[f2]:
                f2+=1
            elif nums1[f1] < nums2[f2]:
                f1+=1
            else:
                return nums1[f1]
        return -1
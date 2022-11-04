# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        maxStr = ""
        res = 0
        nums2Str = "".join([chr(num) for num in nums2])
        for n in nums1:
          maxStr += chr(n)
          if maxStr in nums2Str:
            res = max(res, len(maxStr))
          else:
            maxStr = maxStr[1:]
        return res
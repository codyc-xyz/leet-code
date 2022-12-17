# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
# If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i, n in enumerate(nums1):
            j = 0
            res = -1
            while j < len(nums2):
                if nums2[j] == n:
                    t = j + 1
                    break
                j += 1
            while t < len(nums2):
                if nums2[t] > nums2[j]:
                    res = nums2[t]
                    break
                t += 1
            ans.append(res)
        return ans
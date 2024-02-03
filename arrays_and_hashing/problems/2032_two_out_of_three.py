# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        n1, n2, n3 = set(nums1), set(nums2), set(nums3)
        nums = n1.union(n2).union(n3)
        ans = []
        for n in nums:
            count = 0
            if n in n1:
                count += 1
            if n in n2:
                count += 1
            if n in n3:
                count += 1
            if count > 1:
                ans.append(n)
        return ans

       
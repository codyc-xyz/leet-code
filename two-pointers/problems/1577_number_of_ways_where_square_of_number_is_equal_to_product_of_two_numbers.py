# Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

# Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
# Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = defaultdict(int)
        n2 = defaultdict(int)
        res = 0
        for n in nums1:
            n1[n ** 2] += 1
        
        for n in nums2:
            n2[n**2] += 1
            
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                res += n1[nums2[i] * nums2[j]]
        
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                res += n2[nums1[i] * nums1[j]]
                
        return res
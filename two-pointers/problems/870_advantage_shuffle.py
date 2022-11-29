# You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

# Return any permutation of nums1 that maximizes its advantage with respect to nums2.

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        advantage = deque()
        for i, n in enumerate(nums2):
            k = 0
            while k < len(nums1) and n >= nums1[k]:
                k += 1

            if k < len(nums1) and nums1[k] > n:
                advantage.append(nums1[k])
                nums1.pop(k)
            else:
                advantage.append(nums1[0])
                nums1.pop(0)
        return advantage
            
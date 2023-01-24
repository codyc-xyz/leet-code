# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        while i < len(nums1):
            arr.append(nums1[i])
            i += 1
        while j < len(nums2):
            arr.append(nums2[j])
            j += 1
            
        n = len(arr)
        if n % 2:
            return arr[n // 2]
        else:
            return (arr[n // 2] + arr[n // 2 - 1]) / 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            B, A = A, B
            
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1
        while True:
            m = (l + r) // 2
            i = half - m - 2
            aLeft = A[m] if m >= 0 else float("-inf")
            aRight = A[m + 1] if (m + 1) < len(A) else float("inf")
            bLeft = B[i] if i >= 0 else float("-inf")
            bRight = B[i + 1] if (i + 1) < len(B) else float("inf")
            
            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                r = m - 1
            else:
                l = m + 1
# You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

# Return any permutation of nums1 that maximizes its advantage with respect to nums2.

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        num1 = sorted(nums1)
        num2 = sorted(nums2)
        hm = {}
        idxs = defaultdict(list)
        unused = []

        for i, n in enumerate(nums2):
            heapq.heappush(idxs[n], i)

        i = j = 0
        while i < len(nums1):
            if num1[i] > num2[j]:
                idx = heapq.heappop(idxs[num2[j]])
                hm[idx] = num1[i]
                j += 1
            else:
                unused.append(num1[i])
            i += 1
      
        ans = [-1] * len(nums1)
        for i, n in enumerate(nums2):
            if i in hm:
                ans[i] = hm[i]
        k = 0
        for i in range(len(ans)):
            if ans[i] == -1:
                ans[i] = unused[k]
                k += 1
        return ans


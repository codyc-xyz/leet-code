# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        i = j = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(heap, ([nums1[i] + nums2[j]], [nums1[i], nums2[j]]))

        ans = []
        while heap and k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1

        return ans

# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        m = len(nums1)
        n = len(nums2)

        ans = []
        visited = set()
        minHeap = [[nums1[0] + nums2[0], 0, 0]]
        visited.add((0, 0))

        while minHeap and k > 0:
            currSum, i, j = heapq.heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and ((i + 1, j) not in visited):
                heapq.heappush(minHeap, [nums1[i + 1] + nums2[j], i + 1, j])
                visited.add((i + 1, j))
            if j + 1 < n and ((i, j + 1) not in visited):
                heapq.heappush(minHeap, [nums1[i] + nums2[j + 1], i, j + 1])
                visited.add((i, j + 1))
            k -= 1
        
        return ans




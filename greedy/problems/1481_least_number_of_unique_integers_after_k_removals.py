# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        heap = []

        for c in count:
            heapq.heappush(heap, [count[c], c])

        while k > 0:
            c, n = heapq.heappop(heap)
            if c > 1:
                heapq.heappush(heap, [c - 1, n])
            k -= 1

        return len(heap)
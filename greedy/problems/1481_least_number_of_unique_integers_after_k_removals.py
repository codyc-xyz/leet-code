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


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        arr = []

        for c in count:
            arr.append(count[c])
        arr.sort()

        for i in range(len(arr)):
            if k >= arr[i]:
                k -= arr[i]
            else:
                return len(arr) - i
        return 0

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        countItems = []
        for c in count:
            countItems.append(count[c])
        countItems.sort()

        for i, n in enumerate(countItems):
            if k >= n:
                k -= n
            else:
                return len(countItems) - i 
        return 0

# Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

# Return true if it is possible. Otherwise, return false.

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        heap = []
        for c in count:
            heap.append([c, count[c]])
        heapq.heapify(heap)
        seen = set()
        addBack = []
        while heap:
            N, countN = heapq.heappop(heap)
            if not seen or N - 1 in seen:
                seen.add(N)
                if countN > 1:
                    addBack.append([N, countN - 1])
            else:
                addBack.append([N, countN])
            if len(seen) == k:
                for num, countNum in addBack:
                    heapq.heappush(heap, [num, countNum])
                addBack = []
                seen = set()

        return False if addBack or seen else True
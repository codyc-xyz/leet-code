# Given an integer array nums and an integer k, modify the array in the following way:

# choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times. You may choose the same index i multiple times.

# Return the largest possible sum of the array after modifying it in this way.

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, n)

        while k > 0:
            curr = heapq.heappop(heap)
            heapq.heappush(heap, -curr)
            k -= 1

        return sum(heap)
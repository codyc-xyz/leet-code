# You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

# Return the string that represents the kth largest integer in nums.

# Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        nums.sort(key=lambda x: int(x))
        return nums[-k]

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        heap = []
        for n in nums:
            heapq.heappush(heap, -int(n))

        while k > 1:
            heapq.heappop(heap)
            k -= 1

        return str(-heap[0])
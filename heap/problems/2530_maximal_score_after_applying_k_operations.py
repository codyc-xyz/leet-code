# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

# In one operation:
# choose an index i such that 0 <= i < nums.length,
# increase your score by nums[i], and
# replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.

# The ceiling function ceil(val) is the least integer greater than or equal to val.

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
           
        ans = 0
        while k > 0:
            curr = heapq.heappop(heap)
            ans += -curr
            heapq.heappush(heap, -math.ceil(-curr / 3))
            k -= 1
        return ans
# You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.

# Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo. 

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10**9+7

        heapq.heapify(nums)

        while k > 0:
            heapq.heappush(nums, heapq.heappop(nums) + 1)
            k -= 1

        ans = 1
        for n in nums:
            ans *= n
            ans %= mod
        return ans 

        
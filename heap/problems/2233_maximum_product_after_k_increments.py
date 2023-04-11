# You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.

# Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo. 

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10**9+7

        nums = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(nums)

        while k > 0:
            n, i = heapq.heappop(nums)
            heapq.heappush(nums, (n + 1, i))
            k -= 1

        nums.sort(key=lambda x: x[1])

        ans = nums[0][0]
        for i in range(1, len(nums)):
            ans *= nums[i][0]
            
        return ans % mod

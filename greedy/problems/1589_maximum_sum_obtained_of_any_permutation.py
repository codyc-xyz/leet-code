# We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.

# Return the maximum total sum of all requests among all permutations of nums.

# Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0 for _ in range(len(nums))]
        mod = 10**9+7
        for s, e in requests:
            for i in range(s, e + 1):
                arr[i] -= 1

        heapq.heapify(arr)
        nums.sort()
        i = len(nums) - 1
        ans = 0
        while arr and arr[0] < 0:
            ans += nums[i] * -arr[0]
            heapq.heappop(arr)
            i -= 1
        return ans % mod
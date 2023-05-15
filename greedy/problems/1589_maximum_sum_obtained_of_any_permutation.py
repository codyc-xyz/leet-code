# We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.

# Return the maximum total sum of all requests among all permutations of nums.

# Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0 for _ in range(len(nums) + 1)]
        mod = 10**9+7
        for s, e in requests:
            arr[s] += 1
            arr[e+1] -= 1

        for i in range(1, len(nums) + 1):
            arr[i] += arr[i - 1]
        arr.sort()
        nums.sort()
        i = len(nums) - 1
        j = len(arr) - 1
        ans = 0
        while j >= 0 and arr[j] > 0:
            ans += nums[i] * arr[j]
            j -= 1
            i -= 1
        return ans % mod
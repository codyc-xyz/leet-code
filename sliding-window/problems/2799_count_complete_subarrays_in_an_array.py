# You are given an array nums consisting of positive integers.

# We call a subarray of an array complete if the following condition is satisfied:

# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.

# A subarray is a contiguous non-empty part of an array.

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        count = len(set(nums))
        ans = 0
        for i in range(N-count+1):
            currSet = set()
            for j in range(i, N):
                currSet.add(nums[j])
                if len(currSet) == count:
                    ans += 1
                elif len(currSet) > count:
                    break
        return ans

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        count = len(set(nums))
        windowStart = ans = 0
        curr = defaultdict(int)
        for windowEnd in range(N):
            curr[nums[windowEnd]] += 1
            while len(curr) == count:
                ans += N - windowEnd
                curr[nums[windowStart]] -= 1
                if curr[nums[windowStart]] == 0:
                    del curr[nums[windowStart]]
                windowStart += 1
        return ans
                

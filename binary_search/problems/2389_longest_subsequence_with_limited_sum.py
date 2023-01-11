# You are given an integer array nums of length n, and an integer array queries of length m.

# Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        
        for q in queries:
            curr = 0
            i = 0
            while curr < q and i < len(nums):
                curr += nums[i]
                if curr > q:
                    ans.append(i)
                elif curr == q or i == len(nums) - 1:
                    ans.append(i + 1)
                i += 1
        return ans

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        ans = []
        for q in queries:
            idx = bisect_right(nums, q)
            ans.append(idx)
        return ans
'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
'''

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        ans = 0
        for c in count:
            curr = count[c]
            if c - 1 in count:
                ans = max(ans, curr + count[c-1])
            if c + 1 in count:
                ans = max(ans, curr + count[c+1])
        return ans

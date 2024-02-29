'''
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

'''
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        count = collections.Counter(nums)
        maxCount = max(count.values())
        ans = 0
        for c in count:
            if count[c] == maxCount:
                ans += maxCount
        return ans
        
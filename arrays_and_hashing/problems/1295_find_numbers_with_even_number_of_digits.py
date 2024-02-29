'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        for n in nums:
            if len(str(n)) % 2:
                continue
            ans += 1
        return ans
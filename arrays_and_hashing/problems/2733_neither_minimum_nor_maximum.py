# Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

# Return the selected integer.

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maxN = max(nums)
        minN = min(nums)

        for n in nums:
            if n is not maxN and n is not minN:
                return n
        return -1
        
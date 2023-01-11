# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = set(nums)
        
        for i in range(0, len(nums)):
            if i not in num:
                return i
        return len(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and i == nums[i]:
            i += 1
        return i
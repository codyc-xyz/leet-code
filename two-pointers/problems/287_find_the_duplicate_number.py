# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                return nums[i]
            hm[nums[i]] = i

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = {}
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] in hm:
                return nums[left]
            hm[nums[left]] = left
            if nums[right] in hm:
                return nums[right]
            hm[nums[right]] = right
            left += 1
            right -= 1
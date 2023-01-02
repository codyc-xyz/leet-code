# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l, i = 0, 1
        while i < len(nums):
            if nums[i] != nums[l]:
                l += 1
                nums[l] = nums[i]
            i += 1
        return l + 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            ans = len(set(nums))
            l = r = 0
            while r < len(nums):
                while r < len(nums) and nums[l] == nums[r]:
                    r += 1
                l += 1
                if l < r and r < len(nums):
                    nums[l], nums[r] = nums[r], nums[l]
                    r += 1
                
            return ans
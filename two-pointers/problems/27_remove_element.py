# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] == val:
                nums.pop(left)
                right -= 1
                left -= 1
            left += 1
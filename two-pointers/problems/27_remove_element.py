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
            
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l, r = 0, len(nums) - 1
  
        if len(nums) < 1:
            return len(nums)
        count = 0
        while l <=  r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                count += 1
            elif nums[l] != val:
                l += 1
            elif nums[r] == val:
                r -= 1
                count += 1 
            
        return len(nums) - count
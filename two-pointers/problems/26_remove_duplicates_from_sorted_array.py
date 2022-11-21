# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.append(nums[i])
            
      
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if left < len(arr):
                nums[left] = arr[left]
                left += 1
            else:
                nums.pop(right)
                right -= 1
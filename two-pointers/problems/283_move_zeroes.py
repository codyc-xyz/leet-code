#  Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """   
        i = pops = 0
        n = len(nums)
        while i + pops < n:
            if nums[i] == 0:
                nums.pop(i)
                pops += 1
            else:
                i += 1
        
        for i in range(pops):
            nums.append(0)
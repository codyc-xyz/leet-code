# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        arr = [None] * len(nums)
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                arr[left] = nums[i]
                left += 1
            else:
                arr[right] = nums[i]
                right -= 1
        return arr
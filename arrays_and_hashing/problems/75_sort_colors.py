# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
            
        for i in range(count[0]):
            nums[i] = 0
            
        for i in range(count[1]):
            nums[i + count[0]] = 1
            
        for i in range(count[2]):
            nums[i + count[0] + count[1]] = 2
        return nums
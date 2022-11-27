# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for i in range(len(nums)):
            if nums[i] == 2:
                blue += 1
            elif nums[i] == 1:
                white += 1
            else:
                red += 1
        for i in range(red):
            nums[i] = 0
        for i in range(white):
            nums[red + i] = 1
        for i in range(blue):
            nums[red + white + i] = 2
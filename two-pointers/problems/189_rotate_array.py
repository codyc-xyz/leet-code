# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr = []
        end = len(nums) - k
        start = len(nums) - k
        i = 0
        while k > 0:
            arr.append(nums[end])
            end += 1
            k -= 1
        
        while i < start:
            arr.append(nums[i])
            i += 1
        
        for j in range(len(nums)):
            nums[j] = arr[j]
            j += 1
        
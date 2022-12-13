# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr = []
        modK = k % len(nums)
        end = len(nums) - modK
        while modK > 0:
            arr.append(nums[end])
            end += 1
            modK -= 1
        
        start = len(nums) - modK
        for i in range(start):
            arr.append(nums[i])
            i += 1
        
        for j in range(len(nums)):
            nums[j] = arr[j]
            j += 1
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        modK = k % len(nums)        
        nums.reverse()
        nums[:modK] = nums[:modK][::-1]
        nums[modK:] = nums[modK:][::-1]
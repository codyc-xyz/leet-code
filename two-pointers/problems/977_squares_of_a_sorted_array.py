# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left, right = 0, len(nums) - 1
        n = len(nums) - 1
        arr = [None] * len(nums)
        while right >= left:
            l = nums[left] * nums[left]
            r = nums[right] * nums[right]
            if l > r:
                arr[n] = l
                left += 1
            else:
                arr[n] = r
                right -= 1
            n -= 1
        return arr
                
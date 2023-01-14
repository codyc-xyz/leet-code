# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = set(nums)
        if target not in n:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        if r < 0:
            left = 0
        elif nums[r] != target:
            left = r + 1
        else:
            left = r
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        if nums[l] == target:
            right = l
        else:
            right = l - 1
        
        return [left, right]
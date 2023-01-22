# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        return target in nums

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def binSearch(l, r):
            while l <= r:
                m = (l + r) // 2
                if m >= len(nums):
                    return False
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return True
            return False
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            m = (l + r) // 2
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m
        pivot = l
        if target >= nums[0]:
            return binSearch(0, pivot)
        else:
            return binSearch(pivot, len(nums) - 1)
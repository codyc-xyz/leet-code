# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.binSearch(nums, target, True), self.binSearch(nums, target, False)
        return [left, right]
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if self.inNums(nums, target):
            l = self.findL(nums, target)
            r = self.findR(nums, target)
            return [l, r]
        
        else:
            return [-1, -1]

    def findR(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return r

    def findL(self, nums, target):
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l

    def inNums(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return True
        return False
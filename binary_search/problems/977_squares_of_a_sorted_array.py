# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        
        nums.sort()
        return nums

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l, r = 0, len(nums) - 1
        ans = deque()
        while l <= r:
            left = nums[l] ** 2
            right = nums[r] ** 2
            if left > right:
                ans.appendleft(left)
                l += 1
            else:
                ans.appendleft(right)
                r -= 1
        return ans
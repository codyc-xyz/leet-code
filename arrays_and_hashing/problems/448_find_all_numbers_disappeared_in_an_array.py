# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [-1] * len(nums)
        ans = []
        for n in nums:
            arr[n - 1] = n
            
        for i, a in enumerate(arr):
            if a == -1:
                ans.append(i + 1)
        
        return ans

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            i = abs(n) - 1
            nums[i] = abs(nums[i]) * -1
                
        for i, n in enumerate(nums):
            if n > 0:
                ans.append(i + 1)
        return ans
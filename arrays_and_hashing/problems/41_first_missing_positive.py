# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        digits = set(nums)
        
        for i in range(1, len(nums) + 2):
            if i not in digits:
                return i
        return 0

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
                
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if 0 <= idx < len(nums):
                if nums[idx] > 0:
                    nums[idx] *= -1
                elif nums[idx] == 0:
                    nums[idx] = float("-inf")
                
        for idx, n in enumerate(nums):
            if n >= 0:
                return idx + 1
        return len(nums) + 1
                
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        j = 1
        prev = None
    
        for i in range(len(nums)):
            if prev == nums[i] or nums[i] <= 0:
                continue
            if j != nums[i]:
                return j
            prev = nums[i]
            j += 1
                
        return j + 1 if nums[-1] == j else j

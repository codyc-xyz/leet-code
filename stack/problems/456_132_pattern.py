# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        minNums = [] 
        minNum = float("inf")
        for i, n in enumerate(nums):
            if n < minNum:
                minNum = n
            minNums.append(minNum)
            
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > stack[-1]:
                if stack.pop() > minNums[i]:
                    return True
            
            stack.append(nums[i])
        return False

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        mid = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < mid:
                return True
            while stack and stack[-1] < nums[i]:
                mid = max(mid, stack.pop())
            stack.append(nums[i])
        return False
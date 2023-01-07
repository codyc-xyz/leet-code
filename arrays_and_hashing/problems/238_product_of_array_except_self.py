# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prodsL = [1]
        prodsR = [1]
        for i in range(len(nums) - 1, 0, -1):
            prodsR.append(prodsR[-1] * nums[i])
        prodsR = prodsR[::-1]
        for i in range(len(nums)):
            if i != 0:
                prodsL.append(prodsL[-1] * nums[i - 1])
            ans.append(prodsL[-1] * prodsR[i])
        return ans

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = postfix = 1
        
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
            
        for i in range(len(nums) -1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
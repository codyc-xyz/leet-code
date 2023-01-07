# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            product = 1
            j, t = 0, i + 1
            while j < i:
                product *= nums[j]
                j += 1
            while t < len(nums):
                product *= nums[t]
                t += 1
            ans.append(product)
        return ans
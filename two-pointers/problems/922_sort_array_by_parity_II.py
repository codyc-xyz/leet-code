# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even, odd = 0, 1
        arr = [None] * len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                arr[even] = nums[i]
                even += 2
            else:
                arr[odd] = nums[i]
                odd += 2
        return arr
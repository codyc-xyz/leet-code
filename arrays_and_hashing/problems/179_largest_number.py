# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i, n in enumerate(nums):
            nums[i] = str(n)
            
        def compare(c1, c2):
            if c1 + c2 > c2 + c1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        
        i = 0
        while nums[i] == '0':
            i += 1
            if i == len(nums):
                return '0'
        return "".join(nums[i:])
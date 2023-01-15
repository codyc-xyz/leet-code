# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. 
# Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# The test cases are generated so that there will be an answer.

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def divideGreater(m):
            res = 0
            for n in nums:
                res += math.ceil(n / m)            
            return res <= threshold
        
        l, r = 1, sum(nums)
        ans = 0
        while l <= r:
            m = (l + r) // 2
            
            if divideGreater(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
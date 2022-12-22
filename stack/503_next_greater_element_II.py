# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. 
# If it doesn't exist, return -1 for this number.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1] * n
        nums = nums + nums
        
        r = len(nums) - 1
        
        while r >= 0:
            while stack and nums[r] >= stack[-1]:
                stack.pop()
            if stack: 
                if r >= len(ans):
                    j = r - n
                    ans[j] = stack[-1]
                else:
                    ans[r] = stack[-1]
            stack.append(nums[r])
            r -= 1
        
        return ans
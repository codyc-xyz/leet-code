# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

class Solution:
    def findUnsortedSubarray(self, nums):
        stack = []
        start = len(nums)
        end = 0

        for i, n in enumerate(nums):
            while stack and stack[-1][1] > n:
                start = min(start, stack.pop()[0])
            stack.append([i, n])
            
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1][1] < nums[i]:
                end = max(end, stack.pop()[0])
            stack.append([i, nums[i]])
        if end == 0 and start == len(nums):
            return 0
        return end - start + 1
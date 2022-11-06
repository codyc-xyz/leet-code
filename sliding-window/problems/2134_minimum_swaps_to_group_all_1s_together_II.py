# A swap is defined as taking two distinct positions in an array and swapping the values in them.

# A circular array is defined as an array where we consider the first element and the last element to be adjacent.

# Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        length = len(nums[:total])
        window = sum(nums[:total])
        res = total - window
        minSwaps = float("inf")
        windowStart, windowEnd = 0, len(nums) - total
        if res == 0:
                return 0
        for i in range(length, len(nums) + length):
            if i >= len(nums) and windowEnd <= len(nums):
                window += nums[windowStart] - nums[windowEnd]
                windowStart += 1
                windowEnd += 1
            else:
                window += nums[i] - nums[i - length]
            minSwaps = min(minSwaps, total - window)
        return minSwaps
            
            
            
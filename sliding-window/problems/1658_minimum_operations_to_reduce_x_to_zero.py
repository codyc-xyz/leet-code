# You are given an integer array nums and an integer x. 
# In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. 
# Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        windowStart = 0
        target = sum(nums) - x
        maxLen = 0
        if target == 0:
            return len(nums)
        for windowEnd in range(len(nums)):
            target -= nums[windowEnd]
            while windowStart <= windowEnd and target < 0:
                target += nums[windowStart]
                windowStart += 1
            if target == 0:
                maxLen = max(maxLen, windowEnd - windowStart + 1)
        if maxLen != 0:
            return len(nums) - maxLen 
        else:
            return -1
                
            
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        currSum = windowStart = 0
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        ans = float('inf')

        for windowEnd in range(len(nums)):
            currSum += nums[windowEnd]
            while currSum > target and windowStart < windowEnd:
                currSum -= nums[windowStart]
                windowStart += 1
            if currSum == target:
                ans = min(ans, len(nums) - (windowEnd - windowStart + 1))

        return ans if ans != float('inf') else -1




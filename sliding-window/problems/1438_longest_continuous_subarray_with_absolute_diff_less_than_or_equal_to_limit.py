# Given an array of integers nums and an integer limit, 
# return the size of the longest non-empty subarray such that the absolute difference 
# between any two elements of this subarray is less than or equal to limit.

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longestSub = windowStart = 0
        minQueue = deque()
        maxQueue = deque()
        for windowEnd in range(len(nums)):
            while minQueue and nums[windowEnd] < minQueue[-1]:
                minQueue.pop()
            while maxQueue and nums[windowEnd] > maxQueue[-1]:
                maxQueue.pop()
            maxQueue.append(nums[windowEnd])
            minQueue.append(nums[windowEnd])                
            while maxQueue[0] - minQueue[0] > limit:
                if maxQueue[0] == nums[windowStart]:
                    maxQueue.popleft()
                if minQueue[0] == nums[windowStart]:
                    minQueue.popleft()
                windowStart += 1
            longestSub = max(longestSub, windowEnd - windowStart + 1)
        return longestSub
    

    
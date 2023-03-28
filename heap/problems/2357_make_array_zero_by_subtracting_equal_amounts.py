# You are given a non-negative integer array nums. In one operation, you must:

# Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
# Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
       
        heapq.heapify(nums)
        ops = 0
        while nums:
            curr = heapq.heappop(nums)
            if curr == 0:
                continue
            ops += 1
            if nums:
                for i in range(len(nums)):
                    if nums[i] >= curr:
                        nums[i] -= curr
        return ops

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
       
        nums = set(nums)

        return len(nums) - 1 if 0 in nums else len(nums)
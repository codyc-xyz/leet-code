# You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)

# Return the minimum number of operations to reduce the sum of nums by at least half.

class Solution:
    def halveArray(self, nums: List[int]) -> int:

        heap = [-n for n in nums]
        heapq.heapify(heap)
        currSum = sum(nums)
        target = currSum / 2
        ops = 0
        while currSum > target:
            num = heapq.heappop(heap)
            num = num / 2
            currSum += num
            heapq.heappush(heap, num)
            ops += 1
        return ops

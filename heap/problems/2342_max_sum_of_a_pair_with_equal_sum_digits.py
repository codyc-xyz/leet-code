# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        digitSums = defaultdict(list)
        for i in range(len(nums)):
            digitSum = 0
            char = str(nums[i])
            for c in char:
                digitSum += int(c)
            heapq.heappush(digitSums[digitSum], -nums[i])

        maxVal = 0
        for d in digitSums:
            if len(digitSums[d]) > 1:
                maxVal = min(maxVal, heapq.heappop(digitSums[d]) + heapq.heappop(digitSums[d]))

        return -maxVal or -1

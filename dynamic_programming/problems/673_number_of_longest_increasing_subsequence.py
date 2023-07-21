# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        lenIncreasing = defaultdict(int)

        def backtrack(i, prev, length):
            if i == N:
                lenIncreasing[length] += 1
                return
            if nums[i] > prev:
                backtrack(i + 1, nums[i], length + 1)
            backtrack(i + 1, prev, length)

        backtrack(0, float('-inf'), 0)
        return lenIncreasing[max(lenIncreasing)]


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        N = len(nums)
        lenLis = [0] * N
        count = [0] * N

        for i in range(N - 1, -1, -1):
            maxLen, maxCnt = 1, 1
            for j in range(i + 1, N):
                if nums[j] > nums[i]:
                    if lenLis[j] + 1 > maxLen:
                        maxLen = lenLis[j] + 1
                        maxCnt = count[j]
                    elif lenLis[j] + 1 == maxLen:
                        maxCnt += count[j]
            lenLis[i] = maxLen
            count[i] = maxCnt

        maxLen = max(lenLis)
        ans = 0
        for i in range(N):
            if lenLis[i] == maxLen:
                ans += count[i]

        return ans

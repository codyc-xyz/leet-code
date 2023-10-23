# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

# A subsequence of an array is obtained by deleting some number of elements(can be zero) from the array, leaving the remaining elements in their original order.

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        if all(n >= 0 for n in nums):
            return sum(nums)
        elif all(n <= 0 for n in nums):
            return max(nums)

        currSum = i = 0
        dp = []
        while i < len(nums):
            end = min(i+k+1, len(nums))
            if i + 1 != end:
                currMax = max(n for n in nums[i+1:end])
            else:
                currMax = nums[end - 1]
            if nums[i] < 0 and dp and dp[-1][0] == nums[i] and (len(dp) < 2 or i - dp[-2][2] <= k):
                dp[-1][2] = i
            elif nums[i] >= 0 or dp and dp[-1][1] == nums[i]:
                currSum += nums[i]
                if dp and dp[-1][0] < 0 and nums[i] < 0 and (len(dp) < 2 or i - dp[-2][2] <= k):
                    currSum -= dp.pop()[0]
                dp.append([nums[i], currMax, i])

            i += 1

        currFront, lastFrontBelowNegIdx = 0, None
        currBack, lastBackBelowNegIdx = -1, None

        for i in range(len(dp)):
            currFront += dp[i][0]
            if currFront < 0:
                lastFrontBelowNegIdx = i
                currFront = 0

        for i in range(len(dp)-1, -1, -1):
            currBack += dp[i][0]
            if currBack < 0:
                lastBackBelowNegIdx = i
                currBack = 0

        print(lastFrontBelowNegIdx, dp, lastBackBelowNegIdx, currSum)

        if lastBackBelowNegIdx and lastFrontBelowNegIdx and lastBackBelowNegIdx <= lastFrontBelowNegIdx:
            tmp1 = tmp2 = currSum
            for j in range(len(dp) - 1, lastBackBelowNegIdx-1, -1):
                tmp1 -= dp[j][0]
            for j in range(lastFrontBelowNegIdx+1):
                tmp2 -= dp[j][0]
            return max(tmp1, tmp2)
        else:
            if lastFrontBelowNegIdx != None:
                for j in range(lastFrontBelowNegIdx+1):
                    currSum -= dp[j][0]
            if lastBackBelowNegIdx != None:
                for j in range(len(dp) - 1, lastBackBelowNegIdx-1, -1):
                    currSum -= dp[j][0]
        return currSum


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        heap = [(-nums[0], 0)]
        ans = nums[0]

        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)
            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heapq.heappush(heap, (-curr, i))
        return ans

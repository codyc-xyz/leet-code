# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

# For chosen indices i0, i1, ..., ik - 1, your score is defined as:

# The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
# Return the maximum possible score.

# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        self.maxScore = 0
        def backtrack(i, k, currSum, minMulti):
            if k == 0:
                self.maxScore = max(self.maxScore, currSum * minMulti)
                return
            if i >= len(nums1):
                return
            backtrack(i + 1, k - 1, currSum + nums1[i], min(minMulti, nums2[i]))
            backtrack(i + 1, k, currSum, minMulti)
        backtrack(0, k, 0, float('inf'))
        return self.maxScore
        
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        nums = [[i, j] for i, j in zip(nums1, nums2)]
        nums.sort(key=lambda x: x[1], reverse = True)

        heap = [nums[i][0] for i in range(k)]
        currSum = sum(heap)
        heapq.heapify(heap)
        ans = currSum * nums[k - 1][1]
        for i in range(k, len(nums)):
            currSum -= heapq.heappop(heap)
            currSum += nums[i][0]
            heapq.heappush(heap, nums[i][0])
            ans = max(ans, currSum * nums[i][1])

        return ans

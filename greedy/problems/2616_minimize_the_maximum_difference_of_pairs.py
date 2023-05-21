# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        l, r = 0, nums[-1] - nums[0]

        while l < r:
            m = (l + r) // 2
            i = 1
            P = p
            while i < len(nums):
                if nums[i] - nums[i - 1] <= m:
                    P -= 1
                    if P == 0:
                        break
                    i += 1
                i += 1
            if P == 0:
                r = m
            else:
                l = m + 1
        return l

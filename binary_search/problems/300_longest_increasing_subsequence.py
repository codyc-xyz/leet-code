# Given an integer array nums, return the length of the longest strictly increasing subsequence.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for n in nums:
            if not LIS or n > LIS[-1]:
                LIS.append(n)
            else:
                l, r = 0, len(LIS) - 1
                while l <= r:
                    m = (l + r) // 2
                    if LIS[m] < n:
                        l = m + 1
                    else:
                        r = m - 1
                LIS[l] = n
        return len(LIS)
# 219 Contains Duplicate II – 
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for i, n in enumerate(nums):
            if n in hm and abs(i - hm[n]) <= k:
                return True
            hm[n] = i
        return False
# O(n) time complexity
            
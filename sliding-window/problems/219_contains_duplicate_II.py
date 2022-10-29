# 219 Contains Duplicate II – 
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    counter += 1
        if counter >= 2:
            return True
        else:
            return False
        
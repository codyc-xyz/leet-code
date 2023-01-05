# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for c in nums:
            if c in hm:
                return True
            else:
                hm[c] = 1
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for c in nums:
            if c in seen:
                return True
            else:
                seen.add(c)
        return False
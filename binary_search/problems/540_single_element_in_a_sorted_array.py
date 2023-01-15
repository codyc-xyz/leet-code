# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            
            if m > 0 and nums[m] == nums[m - 1]:
                if not (m - 1) % 2:
                    l = m + 1
                else:
                    r = m - 2
            elif m < len(nums) - 1 and nums[m] == nums[m + 1]:
                if not (len(nums) - (m + 1) - 1) % 2:
                    r = m - 1
                else:
                    l = m + 1
            else:
                return nums[m]
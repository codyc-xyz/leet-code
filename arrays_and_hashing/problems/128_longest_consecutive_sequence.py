# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        consec, ans = 1, 0
        
        for n in nums:
            if n - 1 not in nums:
                j = n
                while j + 1 in nums:
                    consec += 1
                    j += 1
                ans = max(ans, consec)
                consec = 1
        return ans
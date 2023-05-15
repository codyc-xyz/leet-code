# You are given a 0-indexed integer array nums.

# Initially, all of the indices are unmarked. You are allowed to make this operation any number of times:

# Pick two different unmarked indices i and j such that 2 * nums[i] <= nums[j], then mark i and j.
# Return the maximum possible number of marked indices in nums using the above operation any number of times.

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, math.ceil(len(nums) / 2)
        marked = set()
        while r < len(nums):
            while r < len(nums) and r in marked:
                r += 1
            while l < r and l in marked:
                l += 1
            if nums[l] * 2 <= nums[r]:
                marked.add(l)
                marked.add(r)
            r += 1
        return len(marked)
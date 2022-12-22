# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

# Return the sum of all subarray ranges of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = deque()
        ans = 0
        
        for i, n in enumerate(nums):
            smallest = n
            largest = n
            right = i
            while right < len(nums):
                smallest = min(smallest, nums[right])
                largest = max(largest, nums[right])
                ans += largest - smallest
                right += 1
        return ans
# Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 

# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        curr = sum(nums) 
        nums.sort()
        i = res = 0

        while i < len(nums):
            if res + nums[i] < curr - nums[i]:
                res += nums[i]
                curr -= nums[i]
            else:
                break
            i += 1

        return nums[i:][::-1]
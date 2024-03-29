# You are given a 2D integer array groups of length n. You are also given an integer array nums.

# You are asked if you can choose n disjoint subarrays from the array nums such that the ith subarray is equal to groups[i] (0-indexed), and if i > 0, the (i-1)th subarray appears before the ith subarray in nums (i.e. the subarrays must be in the same order as groups).

# Return true if you can do this task, and false otherwise.

# Note that the subarrays are disjoint if and only if there is no index k such that nums[k] belongs to more than one subarray. A subarray is a contiguous sequence of elements within an array.

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        k = i = j = 0
        while i < len(nums):
            if nums[i] == groups[j][k]:
                I = i
                while I < len(nums) and k < len(groups[j]) and nums[I] == groups[j][k]:
                    I += 1
                    k += 1
                if k == len(groups[j]):
                    j += 1
                    i = I - 1
                if j == len(groups):
                    return True
                k = 0
            i += 1
        return False
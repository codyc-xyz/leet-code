# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

# Return any such subsequence as an integer array of length k.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    
        K = k
        res = []
        i = 0
        while K > 0:
            res.append(nums[i])
            i += 1
            K -= 1

        if i == len(nums):
            return res
        
        while i < len(nums):
            currMin = min(res)
            if nums[i] > currMin:
                res.pop(res.index(currMin))
                res.append(nums[i])

            i += 1
        return res

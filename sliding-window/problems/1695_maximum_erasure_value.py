# You are given an array of positive integers nums and want to erase a subarray containing unique elements. 
# The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxScore = score = 0
        sub = []
        for i in range(len(nums)):
            sub.append(nums[i])
            if len(set(sub)) == len(sub):
                score = sum(sub)
                maxScore = max(maxScore, score)
            while len(set(sub)) != len(sub):
                sub.pop(0)
        return maxScore




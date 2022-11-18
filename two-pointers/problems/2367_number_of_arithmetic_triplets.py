# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. 
# A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        hm = {}
        for i in range(len(nums)):
            if (nums[i] - diff in hm) and (nums[i] - (diff + diff)) in hm:
                count += 1
            hm[nums[i]] = i
        return count
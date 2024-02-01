# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

# Return the total number of bad pairs in nums.

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] != j - i:
                    ans += 1
        return ans

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hm = {}
        res = 0
        pairs = len(nums) * (len(nums) - 1) / 2
        for i in range(len(nums)):
            if nums[i] - i in hm:
                res += hm[nums[i] - i]
                hm[nums[i] - i] += 1
            else:
                hm[nums[i] - i] = 1
            
        return int(pairs - res)
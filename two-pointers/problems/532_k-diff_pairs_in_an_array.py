# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

# 0 <= i, j < nums.length
# i != j
# nums[i] - nums[j] == k

# Notice that |val| denotes the absolute value of val.

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = collections.Counter(nums)
        ans = 0
        
        for i in count:
            if (k != 0 and i + k in count) or (k == 0 and count[i] > 1):
                ans += 1
        return ans
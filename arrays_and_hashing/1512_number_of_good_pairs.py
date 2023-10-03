# Given an array of integers nums, return the number of good pairs.

# A pair(i, j) is called good if nums[i] == nums[j] and i < j.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    ans += 1

        return ans


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        ans = 0

        for c in count:
            ans += count[c] * (count[c] - 1) // 2

        return ans

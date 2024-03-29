# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    ans[i] += 1
        return ans

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        N = sorted(nums)
        ans = [0 for _ in range(len(nums))]
        hm = {}
        prev = None
        for i in range(len(N)):
            if N[i] == prev:
                continue
            else:
                hm[N[i]] = i
                prev = N[i]

        for i, n in enumerate(nums):
            ans[i] = hm[n]
        return ans

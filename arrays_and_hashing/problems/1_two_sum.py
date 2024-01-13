# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i, n in enumerate(nums):
            t = target - n
            if t in hm:
                return [hm[t], i]
            else:
                hm[n] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            nums[i] = [n, i]

        nums.sort()
        l, r = 0, len(nums) - 1

        while nums[l][0] + nums[r][0] != target:
            curr = nums[l][0] + nums[r][0]
            if curr > target:
                r -= 1
            else:
                l += 1

        return [nums[l][1], nums[r][1]]

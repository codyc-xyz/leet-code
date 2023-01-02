# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            while i > 0 and i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
            target = nums[i]
            left, right = i + 1, len(nums) - 1
            while right > left:
                if nums[right] + nums[left] + target > 0:
                    right -= 1
                elif nums[right] + nums[left] + target < 0:
                    left += 1
                else:  
                    res.append([nums[left], nums[i], nums[right]])
                    right -= 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
            i += 1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum == 0:
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    l += 1
        return ans
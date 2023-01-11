# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                j = k = mid
                while j > 0 and nums[j - 1] == target:
                    j -= 1
                while k < len(nums) - 1 and nums[k + 1] == target:
                    k += 1
                for i in range(j, k + 1):
                    ans.append(i)
                return ans
                
        return ans
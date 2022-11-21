# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        queue = deque()
        k = 0
        for i in range(len(nums)):
            if nums[i] not in queue:
                queue.append(nums[i])
                k += 1
        d = 0
        while queue:
            nums[d] = queue.popleft()
            d += 1
        
        a = len(nums) - 1
        
        while a >= k:
            nums.pop(k)
            a -= 1
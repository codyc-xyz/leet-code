# You are given a 0-indexed integer array nums. The array nums is beautiful if:
# nums.length is even.
# nums[i] != nums[i + 1] for all i % 2 == 0.

# Note that an empty array is considered beautiful.

# You can delete any number of elements from nums. When you delete an element, 
# all the elements to the right of the deleted element will be shifted one unit to the left to fill the gap created and all the elements to the left of the deleted element will remain unchanged.

# Return the minimum number of elements to delete from nums to make it beautiful.

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        deletions = 0
        for i, n in enumerate(nums):
            
            if stack and n == stack[-1][0] and stack[-1][1] % 2 == 0:
                deletions += 1
                continue
            stack.append([n, len(stack)])
            
        if len(stack) % 2 == 1:
            deletions += 1
        
        return deletions
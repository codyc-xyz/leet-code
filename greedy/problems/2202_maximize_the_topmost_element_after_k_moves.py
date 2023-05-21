# You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

# In one move, you can perform either of the following:

# If the pile is not empty, remove the topmost element of the pile.
# If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
# You are also given an integer k, which denotes the total number of moves to be made.

# Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:

        if len(nums) == 1 and k % 2:
            return -1
        ans = max(nums[:k + 1])
        if nums.index(ans) != k - 1:
            return ans
        else: 
            nums[k - 1] = -1
            return max(nums[:k + 1])
# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should rearrange the elements of nums such that the modified array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.

# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = 0, 1
        arr = [None] * len(nums) 
        for i in range(len(nums)):
            if nums[i] > 0:
                arr[positive] = nums[i]
                positive += 2
            else:
                arr[negative] = nums[i]
                negative += 2
        return arr
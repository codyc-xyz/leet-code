# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:

    def __init__(self, nums: List[int]):
        self.pSum = [0]
        for n in nums:
            self.pSum.append(self.pSum[-1] + n)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.pSum[right+1] - self.pSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
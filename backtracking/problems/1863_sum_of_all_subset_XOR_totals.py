# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:


        self.total = 0

        def backtracking(i, path):
            curr = 0
            for p in path:
                curr = curr ^ p
            self.total += curr
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtracking(j + 1, path)
                path.pop()
        
        backtracking(0, [])
        return self.total
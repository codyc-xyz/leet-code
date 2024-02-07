# You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].

# Return the maximum strength of a group the teacher can create.

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
        nums.sort()
        self.ans = float('-inf')
        def backtrack(i, res, path):
            if i == len(nums):
                if path:
                    self.ans = max(self.ans, res)
                return 
            backtrack(i+1, res, path)
            res *= nums[i]
            path.add(nums[i])
            backtrack(i+1, res, path)
        backtrack(0, 1, set())
        return self.ans

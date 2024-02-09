# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        self.longestPath = 0
        self.ans = []
        def backtrack(i, path):
            if i == len(nums):
                lenPath = len(path)
                if lenPath > self.longestPath:
                    self.ans = path[:]
                    self.longestPath = lenPath
                return
            flag = True
            for n in path:
                if n % nums[i] and nums[i] % n:
                    flag = False
                    break
            if flag:
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
            backtrack(i+1, path)
        backtrack(0, [])
        return self.ans

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            ans.extend(perms)
            nums.append(n)
        return ans

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path)
                return
            for c in nums:
                if c not in path:
                    path.append(c)
                    backtrack(path[:])
                    path.pop()
        backtrack([])
        return ans


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def backtrack(i, res):
            if i == len(nums):
                self.ans.append(res)
                return
            for n in nums:
                if n not in res:
                    backtrack(i + 1, res + [n])

        backtrack(0, [])
        return self.ans

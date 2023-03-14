# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        self.ans = ""
        nums = set(nums)
        def backtrack(curr):
            if self.ans:
                return
            if len(curr) == len(nums):
                res = "".join(curr)
                if res not in nums:
                    self.ans = res
                return
            curr.append('0')
            backtrack(curr)
            curr.pop()
            curr.append('1')
            backtrack(curr)
            curr.pop()
        backtrack([])
        return self.ans
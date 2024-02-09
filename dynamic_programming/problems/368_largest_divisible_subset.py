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

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        cache = {}
        def dfs(i, prev):
            if i == N:
                return []
            if (i, prev) in cache:
                return cache[(i, prev)]
            res = dfs(i+1, prev)
            if not nums[i] % prev:
                tmp = [nums[i]] + dfs(i+1, nums[i])
                res = tmp if len(tmp) > len(res) else res
            cache[(i, prev)] = res
            return cache[(i, prev)]
        return dfs(0, 1)

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        cache = {}
        def dfs(i):
            if i == N:
                return []
            if i in cache:
                return cache[i]
            res = [nums[i]]
            for j in range(i+1, N):
                if not nums[j] % nums[i]:
                    tmp = [nums[i]] + dfs(j)
                    if len(tmp) > len(res):
                        res = tmp
            cache[i] = res
            return cache[i]
        res = []
        for i in range(N):
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp
        return res

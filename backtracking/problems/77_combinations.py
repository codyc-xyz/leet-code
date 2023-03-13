# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        res = []
        def backtrack(path):
            if len(path) == k and set(path) not in res:
                ans.append(path)
                res.append(set(path))
                return
            if len(path) == k:
                return
            for i in range(1, n + 1):
                if i not in path:
                    path.append(i)
                    backtrack(path[:])
                    path.pop()
        backtrack([])
        return ans
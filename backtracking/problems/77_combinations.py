# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(path, j):
            if len(path) == k and path not in ans:
                ans.append(path.copy())
                return
            elif len(path) >= k:
                return
            for i in range(j, n + 1):
                if i not in path:
                    path.add(i)
                    backtrack(path, i + 1)
                    path.remove(i)
        backtrack(set(), 1)
        return ans
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(path, j):
            if len(path) == k:
                ans.append(path.copy())
                return
            for i in range(j, n + 1):
                if i not in path:
                    path.add(i)
                    backtrack(path, i + 1)
                    path.remove(i)
        backtrack(set(), 1)
        return ans
    

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []

        def backtrack(N, K, curr):
            if K == 0:
                self.ans.append(curr)
                return
            if N > n:
                return

            backtrack(N+1, K - 1, curr + [N])
            backtrack(N+1, K, curr)

        backtrack(1, k, [])
        return self.ans

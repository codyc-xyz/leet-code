# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.


class Solution:
    def countArrangement(self, n: int) -> int:

        res = []

        def backtrack(path):
            if len(path) == n:
                res.append(path)
                return
            for j in range(1, n + 1):
                if j not in path:
                    backtrack(path + [j])
                    
        backtrack([])
        ans = 0
        for r in res:
            flag = False
            for i, n in enumerate(r):
                if (i + 1) % n and n % (i + 1):
                    flag = True
                    break
            if flag == False:
                ans += 1
        return ans

class Solution:
    def countArrangement(self, n: int) -> int:

        self.ans = 0

        def backtrack(path):
            if len(path) == n:
                self.ans += 1
                return
            for j in range(1, n + 1):
                if j not in path and ((j == 0) or ((len(path) + 1) % j == 0) or (j % (len(path) + 1) == 0)):

                    backtrack(path + [j])
        backtrack([])
        return self.ans
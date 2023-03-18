# Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

# Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        ans = set()
        def backtrack(path):
            if len(path) == n:
                ans.add(int("".join(path)))
                return
            minus = int(path[-1]) - k
            plus = int(path[-1]) + k
            if minus >= 0:
                backtrack(path + [str(minus)])

            if plus < 10:
                backtrack(path + [str(plus)])
            
        for i in range(1, 10):
            backtrack([str(i)])
        return ans
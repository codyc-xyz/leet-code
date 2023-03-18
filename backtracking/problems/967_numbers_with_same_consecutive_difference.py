# Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

# Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        ans = []
        def backtrack(path):
            if len(path) == n:
                ans.append(int("".join(path)))
                return
            
            for i in range(10):
                if not path:
                    if i > 0:
                        backtrack(path + [str(i)])
                else:
                    if abs(int(path[-1]) - i) == k:
                        backtrack(path + [str(i)])
        backtrack([])
        return ans
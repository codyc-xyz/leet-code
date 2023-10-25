# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth(1-indexed) symbol in the nth row of a table of n rows.

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def dfs(n, k, rootVal):
            if n == 1:
                return rootVal
            totalNodes = 2**(n-1)
            if k <= totalNodes / 2:
                if rootVal == 0:
                    return dfs(n-1, k, 0)
                else:
                    return dfs(n-1, k, 1)
            else:
                if rootVal == 0:
                    return dfs(n-1, k - (totalNodes / 2), 1)
                else:
                    return dfs(n-1, k - (totalNodes / 2), 0)

        return dfs(n, k, 0)

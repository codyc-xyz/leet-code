# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:   
        ans = []

        def backtrack(i, currSum, path):
            if currSum > n or len(path) > k:
                return
            elif currSum == n and len(path) == k:
                ans.append(path)
                return
            elif currSum == n or len(path) == k:
                return
            for j in range(i, 10):
                backtrack(j + 1, currSum + j, path + [j])

        backtrack(1, 0, [])
        return ans
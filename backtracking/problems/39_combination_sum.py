# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        def backtrack(i, currSum, path):
            if currSum > target or i >= len(candidates):
                return
            if currSum == target:
                ans.append(path)
                return
            path.append(candidates[i])
            backtrack(i, currSum + candidates[i], path[:])
            path.pop()
            backtrack(i + 1, currSum, path[:])
        backtrack(0, 0, [])
        return ans

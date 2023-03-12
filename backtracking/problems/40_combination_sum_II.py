# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        if sum(candidates) < target:
            return ans
        candidates.sort()

        def backtrack(i, currSum, path):
            if currSum > target or i >= len(candidates) or currSum + candidates[i] > target:
                return
            if currSum == target:
                ans.append(path)
                return
            path.append(candidates[i])
            if currSum + candidates[i] == target:
                ans.append(path)
                return
            backtrack(i + 1, currSum + candidates[i], path[:])
            path.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, currSum, path[:])
        backtrack(0, 0, [])
        return ans
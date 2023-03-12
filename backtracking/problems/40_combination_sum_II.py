# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(i, currSum, path):
            if i >= len(candidates) or currSum > target:
                return
            if currSum == target and path not in ans:
                ans.append(path)
                return
            path.append(candidates[i])
            if currSum + candidates[i] == target and path not in ans:
                ans.append(path)
                return
            
            backtrack(i + 1, currSum + candidates[i], path[:] )
            path.pop()
            backtrack(i + 1, currSum, path[:])
        
        backtrack(0, 0, [])
        return ans